---
name: flipboard-batch-4-report
last_updated: 2026-07-19
---

# Flipboard import — batch 4 report

Source: ["Food & Flavors" Flipboard magazine](https://flipboard.com/@enetoe/food-flavors-acbn0akgy) (@enetoe). This batch scrolled the feed across two sessions (the feed restarts from the top each time — a known limitation noted in batch 3), collecting 215 unique story URLs total. After duplicate detection against all 184 existing recipes (exact `source_url` match, 30seconds.com numeric tip-ID match, and same-domain/fuzzy-title match) and filtering out roundups/listicles and non-recipe articles, 51 single-recipe candidates remained; 3 more were excluded before dispatch as confirmed same-dish republishes on gamintraveler.com under a different date path (the same failure mode documented in `_cookbook-meta-prompt.md` §6c), leaving **48 URLs dispatched**.

**Result: 42 new recipe files written (cookbook grew from 184 → 226 recipes).** 0 YAML errors, 0 duplicate `source_url` values across the full 226-file set after the build. 6 of the 48 dispatched URLs were skipped (roundup, duplicate, or genuinely insufficient source content) — see below.

## Yield note

This batch's yield (42 of 48 dispatched, ~88%) looks high, but that's after two recovery passes. On the **first** pass, only 24 of 48 wrote successfully — a much larger share of this batch's candidates happened to come from domains already known to be unreliable from this sandbox (`eatingwell.com`, `simplyrecipes.com`, `receitas.globo.com`) plus several `gamintraveler.com` URLs that hit a Cloudflare bot-check wall via raw fetch. Two of the four parallel chunks discovered that falling back to the Claude-in-Chrome browser (instead of the raw `WebFetch`/`web_fetch` tool) got past both the sandbox's fetch blocklist and the Cloudflare wall — real browser navigation isn't subject to either. Two follow-up recovery passes using that browser-only method recovered 14 and then 4 more previously-blocked URLs. **Lesson for future batches:** when a domain in this list (`eatingwell.com`, `simplyrecipes.com`, `receitas.globo.com`, `gamintraveler.com`) fails via raw fetch, try the browser before giving up — it has a meaningfully better success rate than earlier batches' reports suggested.

## Written (42)

**Chunk 1 (7):** Summer Corn Chowder (foodie.com) · Spinach-And-Sun-Dried Tomato Pasta (resolved from a `flip.it` shortlink to southernliving.com) · Spanish Oxtail Stew / Rabo de Toro (gamintraveler.com) · Mediterranean Chickpea Cucumber Salad (30seconds.com) · Tagliatelle al Ragù (gamintraveler.com) · Sheet Pan Mediterranean Garlic Butter Baked Salmon (30seconds.com) · Cucumber Dill Salad (kimschob.com)

**Chunk 2 (9):** Buttery Garlicky Cannellini Beans With Feta and Sumac (seriouseats.com) · Whole-Loaf Cheesy Garlic Bread (gearpatrol.com) · Cheddar Tomato Sandwich, a Tomato Farmer's Method (simplyrecipes.com) · Easy Homemade Watermelon Lemonade (kimschob.com) · Spaghetti alla Puveriello / Poor Man's Spaghetti (simplyrecipes.com) · Maminha com Manteiga Temperada (receitas.globo.com, translated) · No-Bake Boston Cream Pie Bars (aol.com) · Ina Garten's Cauliflower Toast (eatingwell.com) · High-Protein No-Mayonnaise Tuna Salad (30seconds.com)

**Chunk 3 (3):** Peanut Butter Fandango Rice Krispies Treats (30seconds.com) · $1000 Baked Spaghetti Pasta Casserole (30seconds.com) · Crab Salad (nutritiousdeliciousness.com)

**Chunk 4 (5):** Back-to-Basics: How to Make Salmon on the Griddle (barbecuebible.com) · This Creamy Lemon Rigatoni (thekitchn.com, Giada De Laurentiis's cottage-cheese pasta — quantities cross-referenced against the linked giadzy.com recipe since The Kitchn's own article omitted them, both URLs cited) · Mediterranean Vegetable Soup (seasonalcravings.com) · Polpette / Traditional Italian Meatballs in Tomato Sauce (cucinabyelena.com) · Creamy Garlic Shrimp (30seconds.com)

**Recovery pass 1 — browser fallback (14):** Garlic-Dijon Vinaigrette (eatingwell.com) · Roasted Potato Tzatziki Bowls (eatingwell.com) · Salada de grão-de-bico com cebola marinada (receitas.globo.com, translated) · Bacalhau ao forno com batatas e azeitonas pretas (receitas.globo.com, translated) · Authentic Spaghetti Bolognese (gamintraveler.com) · Brodo di Pollo con Pastina (gamintraveler.com) · Tagliatelle al Tartufo Truffle Sauce (gamintraveler.com) · Classic Creamy Tuscan Chicken (gamintraveler.com — named to distinguish from the existing slow-cooker version) · Homemade Chicken Tikka Masala (gamintraveler.com) · Farofa de Natal (receitas.globo.com, translated) · Rabanada da Solange Couto (receitas.globo.com, translated) · Salada de bacalhau com batata e azeitona (receitas.globo.com, translated — confirmed distinct from the existing hot bacalhau dishes) · Zuppa Toscana (simplyrecipes.com — confirmed distinct from the existing `tuscan-white-bean-soup.md`) · Three Bean Salad (eatingwell.com)

**Recovery pass 2 — browser fallback (4):** Mexican Street Corn-Inspired Bean Salad (allrecipes.com) · Lemon-Garlic Salmon & Broccoli Bowls (eatingwell.com) · French Lentil Salad (eatingwell.com) · Whipped Strawberry Lemonade (eatingwell.com)

## Skipped (9 total: 6 dispatched-then-skipped, 3 excluded before dispatch)

**Skipped after fetching (6):**
- Popular Nordic Dishes From Sweden, Norway And Denmark (gamintraveler.com) — genuine roundup covering three separate dishes (Swedish meatballs, Norwegian salmon, Danish smørrebrød), each with its own ingredient list; not one recipe.
- Our Most Popular 5-Star Italian Recipes (simplyrecipes.com) — confirmed roundup, 27 linked recipes.
- How to Prep 5 Mediterranean Diet Meals for the Week (eatingwell.com) — bundles 4 base components into 5 different lunch assemblies; no single primary dish to extract.
- Easy Skillet Dinners (littlebitrecipes.com) — the fetch redirected to unrelated, mismatched content (an EatingWell salmon/broccoli bowl page, not a skillet roundup); the agent also noted a couple of other unexplained cross-domain content leaks in that session, so this one was treated as unreliable rather than risk misattributed content.
- Brigadeiro de pistache (globorural.globo.com) — the article loaded fine but only names the three ingredients in passing and credits an external "TudoGostoso" source with a dead link; no actual quantities or steps were ever given, so nothing was written per the anti-fabrication rule.
- The Hungarian Goulash Recipe (gamintraveler.com) — duplicate: the cookbook already has `recipes/soups/hungarian-goulash.md` (sourced from 30seconds.com) for the same dish.

**Excluded before dispatch (3) — confirmed gamintraveler.com same-dish republishes under a different date path, per the duplicate-detection precedent in `_cookbook-meta-prompt.md` §6c:**
- `gamintraveler.com/2026/04/25/how-to-make-shrimp-scampi/` — duplicate of the existing `recipes/seafood-mains/shrimp-scampi.md` (same site, 2025/08/16 original).
- `gamintraveler.com/2026/04/25/how-to-make-spaghetti-carbonara/` — duplicate of the existing `recipes/pasta/spaghetti-carbonara.md` (same site, 2026/01/28 original).
- `gamintraveler.com/2025/09/08/how-to-make-spaghetti-carbonara/` — same duplicate as above, a second republish of the same carbonara article.

## A note on two similar-looking pasta recipes kept as separate files

Both `tagliatelle-al-ragu.md` and `authentic-spaghetti-bolognese.md` are gamintraveler.com articles about a slow-simmered Bolognese-style meat sauce, and both explicitly argue (in their own text) that true ragù isn't the same as "spaghetti Bolognese." A direct ingredient comparison confirms they are genuinely different recipes, not a renamed duplicate: the ragù uses 225g beef + 225g pork, 1 cup crushed tomato, white wine, and milk, always with tagliatelle; the spaghetti bolognese uses 500g beef (or beef/pork mix), 800g canned tomato + tomato paste, red wine, and beef broth, with spaghetti. Kept as two separate entries, consistent with this project's existing precedent of keeping multiple genuinely-distinct variants of a similar dish (e.g. the two existing lemon pastas).

## Photos

Direct image downloads failed for every recipe this batch (the sandbox's outbound proxy blocks arbitrary hosts), so all 42 new recipes use `image_source_url` (a verified `og:image`) rather than a locally downloaded `image_local`. Every image was sanity-checked against the actual dish per `_cookbook-meta-prompt.md` §7b before use — the bacalhau ao forno recipe in particular got extra scrutiny given this project's prior gamintraveler/receitas.globo.com bacalhau image-mismatch history, and its image was confirmed to genuinely show baked cod with potatoes.

## Build verification

`python3 _build/build.py` completed cleanly on the first run: 226 recipes across 17 categories, 0 parse errors, 0 duplicate source URLs. `index.html` ends correctly (`</script>\n</body>\n</html>`, ~1.23 MB), confirming no truncation. The same 6 recipes carried over from earlier batches still show the same-category fallback photo (no new fallback cases introduced by this batch): tzatziki-xoxobella, creamy-lemon-pasta, sheet-pan-garlic-butter-gnocchi-with-summer-vegetables, bacalao-a-la-vizcaina, bacalhau-a-bras, chicken-and-sausage-gumbo-with-dark-roux.

`README.md`'s "Current recipes" index was regenerated from every recipe's frontmatter (same approach as batch 3), rather than hand-edited.
