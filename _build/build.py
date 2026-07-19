#!/usr/bin/env python3
"""
Our Cookbook -- static site generator.

Reads every recipe Markdown file under recipes/**/*.md, parses YAML
frontmatter + the fixed section structure defined in
_cookbook-meta-prompt.md, and regenerates a single standalone index.html
at the project root with all recipe data embedded inline (no server,
no external fetch of local files -- works by double-clicking the file).

Also converts ingredient quantities between unit systems at build time:
metric (grams/mL) is the primary display unit, US customary (cups,
tablespoons, teaspoons, oz, lb) is shown as a secondary reference in
parentheses. Recipe Markdown files are left exactly as sourced -- this
conversion happens only in the generated HTML, never by editing the .md.

Run after adding/editing any recipe:
    python3 _build/build.py

This script only reads recipes/*.md and writes index.html. It never
touches the source Markdown files, so re-running it is always safe.
"""
import json
import re
import sys
from pathlib import Path
from datetime import datetime

import yaml

ROOT = Path(__file__).resolve().parent.parent
RECIPES_DIR = ROOT / "recipes"
TEMPLATE_PATH = Path(__file__).resolve().parent / "template.html"
OUTPUT_PATH = ROOT / "index.html"

SECTION_ORDER = [
    "Description",
    "Ingredients",
    "Instructions",
    "Cook's Notes & Tips",
    "My Notes",
    "Missing Information",
    "Source",
]

# Units recognized when splitting a quantity from an ingredient line.
UNIT_WORDS = [
    "tablespoons", "tablespoon", "tbsp", "teaspoons", "teaspoon", "tsp",
    "cups", "cup", "ounces", "ounce", "oz", "pounds", "pound", "lbs", "lb",
    "grams", "gram", "g", "kilograms", "kilogram", "kg", "milliliters",
    "milliliter", "ml", "liters", "liter", "l", "cloves", "clove",
    "slices", "slice", "pinch", "pinches", "dash", "dashes", "cans", "can",
    "fillets", "fillet", "sprigs", "sprig", "bunches", "bunch",
]
UNIT_PATTERN = r"\b(?:" + "|".join(sorted(UNIT_WORDS, key=len, reverse=True)) + r")\b"

# Matches a leading quantity like "1 1/2", "2", "1/3", "3-4" (range kept as text)
QTY_PATTERN = re.compile(
    r"^\s*(?P<qty>\d+\s+\d+/\d+|\d+/\d+|\d+(?:\.\d+)?)\s*"
    r"(?P<unit>" + UNIT_PATTERN + r")?\s*"
)

# ---------------------------------------------------------------------------
# Unit conversion: metric primary, US customary secondary.
#
# Volume/weight-unit definitions below are exact US customary conversions
# (1 US cup = 236.588 mL, 1 tbsp = 14.7868 mL, 1 tsp = 4.92892 mL,
# 1 oz = 28.3495 g, 1 lb = 453.592 g) -- standard, non-ingredient-specific
# facts, not sourced from any single recipe site.
#
# Ingredient densities (grams per US cup) are sourced from King Arthur
# Baking's Ingredient Weight Chart:
# https://www.kingarthurbaking.com/learn/ingredient-weight-chart
# (retrieved 2026-07-15), except "water", which uses the physical
# near-1g/mL density of water at room temperature.
# ---------------------------------------------------------------------------

ML_PER_CUP = 236.588
ML_PER_TBSP = 14.7868
ML_PER_TSP = 4.92892
G_PER_OZ = 28.3495
G_PER_LB = 453.592

US_VOLUME_UNITS = {
    "cup": ML_PER_CUP, "cups": ML_PER_CUP,
    "tablespoon": ML_PER_TBSP, "tablespoons": ML_PER_TBSP, "tbsp": ML_PER_TBSP,
    "teaspoon": ML_PER_TSP, "teaspoons": ML_PER_TSP, "tsp": ML_PER_TSP,
}
US_WEIGHT_UNITS = {
    "oz": G_PER_OZ, "ounce": G_PER_OZ, "ounces": G_PER_OZ,
    "lb": G_PER_LB, "lbs": G_PER_LB, "pound": G_PER_LB, "pounds": G_PER_LB,
}
METRIC_WEIGHT_UNITS = {"g", "gram", "grams", "kg", "kilogram", "kilograms"}
METRIC_VOLUME_UNITS = {"ml", "milliliter", "milliliters", "l", "liter", "liters"}
NON_CONVERTIBLE_UNITS = {
    "cloves", "clove", "slices", "slice", "pinch", "pinches", "dash", "dashes",
    "cans", "can", "fillets", "fillet", "sprigs", "sprig", "bunches", "bunch",
}

# Grams per US cup. Checked in order -- first keyword match in the
# ingredient's text wins, so more specific entries must come before
# generic ones (e.g. "brown sugar" before "sugar").
DENSITY_G_PER_CUP = [
    (["brown sugar"], 213),
    (["confectioners", "powdered sugar"], 113),
    (["granulated sugar", "sugar"], 198),
    (["all-purpose flour", "bread flour", "flour"], 120),
    (["butter"], 226),
    (["cornstarch"], 112),
    (["feta"], 114),
    (["cheddar", "mozzarella", "parmesan", "grated cheese", "shredded cheese", "cheese"], 113),
    (["heavy cream", "cream"], 227),
    (["honey"], 336),
    (["garlic"], 224),
    (["lemon juice"], 224),
    (["table salt", "fine salt", "salt"], 288),
    (["olive oil"], 200),
    (["vegetable oil", "oil"], 198),
    (["blueberr"], 155),
    (["water"], 236.6),
]


def lookup_density(ingredient_text: str):
    low = ingredient_text.lower()
    for keywords, grams_per_cup in DENSITY_G_PER_CUP:
        if any(k in low for k in keywords):
            return grams_per_cup
    return None


# ---------------------------------------------------------------------------
# Difficulty normalization: recipe files may record difficulty in whatever
# wording the source used (or the user typed). The site always shows one of
# exactly three levels -- Easy / Moderate / Hard -- as an icon-plus-label, so
# free text is mapped to a level here at build time. Unrecognized wording is
# kept as the label text but gets no filled bars (level=None); truly missing
# difficulty is None/None and the site displays "N.A."
# ---------------------------------------------------------------------------

def normalize_difficulty(raw):
    if not raw or not str(raw).strip():
        return None, None
    low = str(raw).strip().lower()
    if any(k in low for k in ("easy", "beginner", "simple")):
        return "Easy", 1
    if any(k in low for k in ("hard", "difficult", "advanced", "expert")):
        return "Hard", 3
    if any(k in low for k in ("moderate", "medium", "intermediate")):
        return "Moderate", 2
    return str(raw).strip(), None


def round_metric(v):
    if v is None:
        return None
    if v < 10:
        return round(v, 1)
    return round(v)


def convert_ingredient(qty, unit, text):
    """
    Returns (metric_qty, metric_unit, us_qty, us_unit, us_computed).
    metric_qty/unit is None when no reliable conversion exists (count-based
    units like "cloves", or no unit at all) -- callers should fall back to
    displaying the original qty/unit in that case.
    """
    if qty is None or not unit:
        return (None, None, None, None, False)

    key = unit.lower()

    if key in NON_CONVERTIBLE_UNITS:
        return (None, None, None, None, False)

    if key in METRIC_WEIGHT_UNITS:
        grams = qty * (1000 if key.startswith("kg") else 1)
        density = lookup_density(text)
        us_qty = us_unit = None
        us_computed = False
        if density:
            cups = grams / density
            if cups >= 0.2:
                us_qty, us_unit = round(cups, 3), "cup"
            elif cups * 16 >= 1:
                us_qty, us_unit = round(cups * 16, 3), "tablespoon"
            else:
                us_qty, us_unit = round(cups * 48, 3), "teaspoon"
            us_computed = True
        return (round_metric(grams), "g", us_qty, us_unit, us_computed)

    if key in METRIC_VOLUME_UNITS:
        ml = qty * (1000 if key.startswith("l") else 1)
        return (round_metric(ml), "mL", None, None, False)

    if key in US_VOLUME_UNITS:
        ml = qty * US_VOLUME_UNITS[key]
        density = lookup_density(text)
        if density:
            grams = ml / ML_PER_CUP * density
            return (round_metric(grams), "g", qty, unit, False)
        return (round_metric(ml), "mL", qty, unit, False)

    if key in US_WEIGHT_UNITS:
        grams = qty * US_WEIGHT_UNITS[key]
        return (round_metric(grams), "g", qty, unit, False)

    return (None, None, None, None, False)


# ---------------------------------------------------------------------------
# Oven temperature conversion: Celsius primary, Fahrenheit secondary.
#
# Conversion formulas (exact): C = (F - 32) * 5/9, F = C * 9/5 + 32.
# Applied to instruction text, cook's notes, description, and the missing-
# info checklist at build time -- the .md source keeps whatever the
# original recipe/user wrote, matching the same principle used for
# ingredient units in build_ingredient conversion above.
# ---------------------------------------------------------------------------

TEMP_PATTERN = re.compile(
    r"(?P<num>\d{2,3})\s*°?\s*(?:degrees?\s*)?(?P<unit>F(?:ahrenheit)?|C(?:elsius)?)\b"
)
DUAL_TEMP_PATTERN = re.compile(
    r"\d{2,3}\s*°?\s*[CF]\s*\(\s*\d{2,3}\s*°?\s*[FC]\s*\)"
)


def f_to_c(f):
    return round((f - 32) * 5 / 9)


def c_to_f(c):
    return round(c * 9 / 5 + 32)


def convert_temperatures(text):
    if not text:
        return text

    protected = []
    placeholder = "@@TEMP{}@@"

    def protect(m):
        protected.append(m.group(0))
        return placeholder.format(len(protected) - 1)

    text = DUAL_TEMP_PATTERN.sub(protect, text)

    def repl(m):
        num = int(m.group("num"))
        unit = m.group("unit")[0].upper()
        if unit == "F":
            c, f = f_to_c(num), num
        else:
            c, f = num, c_to_f(num)
        return "{}°C ({}°F)".format(c, f)

    text = TEMP_PATTERN.sub(repl, text)

    def restore(m):
        return protected[int(m.group(1))]

    text = re.sub(r"@@TEMP(\d+)@@", restore, text)
    return text


def parse_fraction(token: str) -> float:
    token = token.strip()
    if " " in token:
        whole, frac = token.split(" ", 1)
        num, den = frac.split("/")
        return float(whole) + float(num) / float(den)
    if "/" in token:
        num, den = token.split("/")
        return float(num) / float(den)
    return float(token)


def parse_ingredient(line: str) -> dict:
    raw = line.strip().lstrip("-").strip()
    m = QTY_PATTERN.match(raw)
    if not m:
        return {
            "raw": raw, "qty": None, "unit": None, "text": raw,
            "metric_qty": None, "metric_unit": None,
            "us_qty": None, "us_unit": None, "us_computed": False,
        }
    qty = parse_fraction(m.group("qty"))
    unit = m.group("unit") or ""
    rest = raw[m.end():].strip()
    metric_qty, metric_unit, us_qty, us_unit, us_computed = convert_ingredient(qty, unit, rest)
    return {
        "raw": raw, "qty": qty, "unit": unit, "text": rest,
        "metric_qty": metric_qty, "metric_unit": metric_unit,
        "us_qty": us_qty, "us_unit": us_unit, "us_computed": us_computed,
    }


def split_sections(body: str) -> dict:
    sections = {}
    current = None
    buf = []
    for line in body.splitlines():
        h2 = re.match(r"^##\s+(.*)$", line.strip())
        if h2:
            if current is not None:
                sections[current] = "\n".join(buf).strip()
            current = h2.group(1).strip()
            buf = []
        elif line.strip().startswith("# ") and current is None:
            continue  # H1 title line, handled separately
        else:
            buf.append(line)
    if current is not None:
        sections[current] = "\n".join(buf).strip()
    return sections


def extract_list_items(section_text: str) -> list:
    items = []
    for line in section_text.splitlines():
        line = line.strip()
        if line.startswith("- "):
            items.append(line[2:].strip())
    return items


def extract_numbered_steps(section_text: str) -> list:
    steps = []
    for line in section_text.splitlines():
        line = line.strip()
        m = re.match(r"^\d+\.\s+(.*)$", line)
        if m:
            steps.append(m.group(1).strip())
    return steps


def parse_recipe_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    fm_match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not fm_match:
        raise ValueError(f"{path}: missing YAML frontmatter")
    frontmatter = yaml.safe_load(fm_match.group(1)) or {}
    body = fm_match.group(2)

    title_match = re.search(r"^#\s+(.*)$", body, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else frontmatter.get("title", path.stem)

    sections = split_sections(body)
    ingredients_raw = extract_list_items(sections.get("Ingredients", ""))
    ingredients = [parse_ingredient(i) for i in ingredients_raw]
    instructions = [convert_temperatures(s) for s in extract_numbered_steps(sections.get("Instructions", ""))]

    image = frontmatter.get("image_local") or frontmatter.get("image_source_url")
    image_is_remote = bool(frontmatter.get("image_source_url")) and not frontmatter.get("image_local")
    if frontmatter.get("image_local"):
        image = "images/" + str(frontmatter["category"]) + "/" + Path(frontmatter["image_local"]).name \
            if not str(frontmatter["image_local"]).startswith("images/") else frontmatter["image_local"]

    slug = path.stem
    difficulty_label, difficulty_level = normalize_difficulty(frontmatter.get("difficulty"))

    return {
        "slug": slug,
        "title": title,
        "category": frontmatter.get("category", "uncategorized"),
        "tags": frontmatter.get("tags") or [],
        "cuisine": frontmatter.get("cuisine"),
        "prep_time_minutes": frontmatter.get("prep_time_minutes"),
        "cook_time_minutes": frontmatter.get("cook_time_minutes"),
        "total_time_minutes": frontmatter.get("total_time_minutes"),
        "servings": frontmatter.get("servings"),
        "difficulty": frontmatter.get("difficulty"),
        "difficulty_label": difficulty_label,
        "difficulty_level": difficulty_level,
        "diet": frontmatter.get("diet") or [],
        "image": image,
        "image_is_remote": image_is_remote,
        "image_is_fallback": False,
        "image_fallback_title": None,
        "description": convert_temperatures(sections.get("Description", "").strip()),
        "ingredients": ingredients,
        "instructions": instructions,
        "cooks_notes": convert_temperatures(sections.get("Cook's Notes & Tips", "").strip()),
        "my_notes": sections.get("My Notes", "").strip(),
        "missing_info": sections.get("Missing Information", "").strip(),
        "source_url": frontmatter.get("source_url"),
        "source_title": frontmatter.get("source_title"),
        "source_author": frontmatter.get("source_author"),
        "incomplete": "UNVERIFIED" in (frontmatter.get("tags") or []),
        "md_path": str(path.relative_to(ROOT)).replace("\\", "/"),
    }


def main():
    if not RECIPES_DIR.exists():
        print(f"No recipes/ folder found at {RECIPES_DIR}", file=sys.stderr)
        sys.exit(1)

    recipes = []
    errors = []
    for md_path in sorted(RECIPES_DIR.rglob("*.md")):
        try:
            recipes.append(parse_recipe_file(md_path))
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{md_path}: {exc}")

    recipes.sort(key=lambda r: (r["category"], r["title"]))

    # ------------------------------------------------------------------
    # Photo fallback -- SAME CATEGORY ONLY, never cross-category.
    #
    # Earlier version of this borrowed *any* recipe's photo cookbook-wide
    # when a category had no photographed peer, which produced genuinely
    # wrong results (e.g. a spaghetti sauce recipe showing a photo of
    # potato croquettes, reported 2026-07-16) -- a labeled caption doesn't
    # fix that, because the image is not actually related to the dish.
    #
    # The rule now: only borrow a photo from another recipe in the SAME
    # category (e.g. another sauce for a sauce), and only ever mark it as
    # a stand-in, never presented as the real dish (see
    # _cookbook-meta-prompt.md #7). If no same-category recipe has a real
    # photo, the recipe shows the plain colored-initials tile instead --
    # an honest "no photo yet" state beats an unrelated one.
    # ------------------------------------------------------------------
    recipes_by_category = {}
    for r in recipes:
        recipes_by_category.setdefault(r["category"], []).append(r)

    for r in recipes:
        if r.get("image"):
            continue
        same_cat = [
            x for x in recipes_by_category.get(r["category"], [])
            if x is not r and x.get("image") and not x.get("image_is_fallback")
        ]
        if same_cat:
            donor = same_cat[0]
            r["image"] = donor["image"]
            r["image_is_remote"] = donor.get("image_is_remote", False)
            r["image_is_fallback"] = True
            r["image_fallback_title"] = donor["title"]
        # else: no same-category donor -- leave image=None, the site
        # falls back to the plain initials tile (see thumbHtml/hero in
        # template.html), never a cross-category photo.

    categories = sorted({r["category"] for r in recipes})

    # Visibility guardrail: always surface which recipes still have no
    # real photo of their own (borrowed or none at all) so this doesn't
    # go unnoticed the way it did before -- see #7 in the meta-prompt.
    no_own_photo = sorted(
        (r["category"], r["slug"], "borrowed same-category photo" if r.get("image_is_fallback") else "no photo at all")
        for r in recipes
        if r.get("image_is_fallback") or not r.get("image")
    )

    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    html = template.replace(
        "/*__RECIPE_DATA__*/",
        json.dumps({"recipes": recipes, "categories": categories}, indent=None),
    ).replace(
        "__GENERATED_DATE__",
        datetime.now().strftime("%Y-%m-%d %H:%M"),
    ).replace(
        "__RECIPE_COUNT__",
        str(len(recipes)),
    )

    OUTPUT_PATH.write_text(html, encoding="utf-8")

    print(f"Built {OUTPUT_PATH} with {len(recipes)} recipe(s) across {len(categories)} categories.")
    if errors:
        print("Warnings:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
    if no_own_photo:
        print(f"\n{len(no_own_photo)} recipe(s) still have no photo of their own "
              f"(see _cookbook-meta-prompt.md #7 for the fallback rule):")
        for category, slug, reason in no_own_photo:
            print(f"  - [{category}] {slug}: {reason}")


if __name__ == "__main__":
    main()
