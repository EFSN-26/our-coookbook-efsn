---
name: cookbook-meta-prompt
version: 1.11
last_updated: 2026-07-17
---

# Digital Cookbook — Operating Meta-Prompt

This document is the standing specification for how this project works. Paste it into a new conversation (or just point Claude at this file) any time you want Claude to add, edit, search, or reorganize recipes — it defines the data format and the workflows so every recipe stays consistent and machine-readable.

## 1. Purpose

A personal, Markdown-based recipe library that supports:
- Adding recipes (typed in, or extracted from a URL)
- Uploading/attaching original photos
- Organizing by category and tag
- Searching by ingredient
- Generating shopping lists
- Editing recipes and adding personal notes
- Scaling ingredient quantities to a different number of servings
- Browsing everything in a standalone, searchable HTML site (`index.html`)

Markdown files under `recipes/` are the single source of truth. `index.html` is a **generated view** of that data — never hand-edited, always rebuilt from the Markdown.

## 2. Why Markdown (and when it would NOT be the right choice)

Markdown is recommended here because:
- It's plain text: readable, editable, and portable without special software, and safe from OneDrive sync corruption issues that can affect binary formats.
- YAML frontmatter (see §4) gives Claude — and the `_build/build.py` generator — structured fields to compute with: servings, times, tags, ingredient quantities.
- It's the native format most static recipe/blog systems use (e.g., Jekyll, Hugo, Eleventy all store recipes as Markdown + frontmatter).
- Git/version-history friendly if you ever put this folder under source control.

Markdown is **not** the right choice if you eventually want multi-user concurrent editing with permissions, relational queries across thousands of recipes, or a mobile app with offline sync — those would call for a real database. For a personal library maintained by one or two people, Markdown is a good fit; this is an architectural judgment call, not a sourced external fact.

## 3. Folder structure

```
Our Coookbook/
├── _cookbook-meta-prompt.md      ← this file
├── README.md                     ← human-readable index/quick start
├── index.html                    ← GENERATED — the standalone browsable/searchable site
├── _build/
│   ├── build.py                  ← generator: recipes/*.md → index.html
│   └── template.html             ← HTML/CSS/JS shell (edit this, not index.html)
├── recipes/
│   ├── salads/
│   ├── seafood-mains/
│   ├── breads/
│   └── <category>/               ← new category folders created as needed
├── images/
│   ├── salads/
│   ├── seafood-mains/
│   ├── breads/
│   └── <category>/               ← mirrors recipes/ folder names
└── shopping-lists/
    └── (generated on request, dated file names)
```

Category = primary cuisine/course grouping. A recipe lives in exactly one category folder; anything cross-cutting (e.g., "gluten-free," "15-minute," "Mediterranean") becomes a **tag** in frontmatter instead, so search isn't limited to folder location.

## 4. Recipe file naming

`kebab-case-descriptive-name.md`, no author names, no dates, no source-site branding. Examples: `peach-blueberry-cucumber-salad-with-feta.md`, `one-pan-salmon-with-creamy-caper-sauce.md`.

## 5. Recipe schema

Every recipe uses this exact structure so any file — and the generator script — can parse it the same way:

```markdown
---
title: 
category: 
tags: []
cuisine: 
prep_time_minutes: 
cook_time_minutes: 
total_time_minutes: 
servings: 
difficulty: 
diet: []
image_local: null            # relative path under /images if a photo is stored locally
image_source_url: null       # original photo URL, used when a local copy isn't available
source_title: 
source_url: 
source_author: 
date_added: 
retrieved_date: 
---

# {Title}

## Description
1-3 sentence intro, drawn from the source or written fresh.

## Ingredients
_(for {servings} servings — see §8 for scaling)_

- {quantity} {unit} {ingredient}, {prep note if any}
- ...

## Instructions
1. Step one.
2. Step two.
...

## Cook's Notes & Tips
Anything from the source about substitutions, technique, or storage.

## My Notes
_(blank — this section is reserved for your own additions; Claude only writes here when you ask it to)_

## Missing Information
_(only present on recipes still tagged `UNVERIFIED` — a short checklist of exactly what's still needed, e.g.:)_
- [ ] Oven temperature and bake time
- [ ] Total proof/rise time

## Source
- Original recipe: [{source_title}]({source_url}) by {source_author}
- Retrieved: {retrieved_date}
```

Keeping every ingredient line in the pattern `quantity unit ingredient` (e.g., "2 cups fresh blueberries") is what makes portion scaling, shopping-list aggregation, **and** the HTML site's live servings-scaling feature possible. Don't collapse ingredients into paragraph prose. Mark an unverified/incomplete recipe by including the tag `UNVERIFIED` — the site automatically shows a warning banner on any recipe carrying that tag.

**`difficulty` field:** write it as whatever wording the source used, or leave it blank if the source didn't state one — never guess it. `build.py` normalizes it at build time into one of exactly three site-displayed levels (Easy / Moderate / Hard, shown as a small filled-bar icon plus label) by keyword-matching the text (e.g. "beginner-friendly" → Easy, "intermediate" → Moderate, "advanced" → Hard). Wording it doesn't recognize is still shown as plain text but without filled bars; a blank field shows "N.A." on the site. This mirrors the unit/temperature pattern in §5b/§5c: the `.md` file keeps the original wording, normalization only happens in the generated HTML.

## 5b. Units — metric (weight) primary, US customary (volume) secondary

**Default:** every ingredient quantity displays as **metric first, US customary second in parentheses** on the site — e.g. `114 g (1 cup) feta cheese`, `22 mL (1½ tbsp) Dijon mustard`. This is a display-time conversion done by `_build/build.py`, not something you or Claude need to do by hand in the Markdown.

**Why build-time, not in the Markdown file:** recipe `.md` files keep recording ingredients exactly as the source gave them — that's what preserves the citation. `build.py` computes both unit systems from whatever's written and embeds both into `index.html`. This means:
- If a source gives US volume (cups, tablespoons, teaspoons, oz, lb), the site shows the computed metric weight as primary and the original US amount as the secondary reference.
- If a source already gives metric (grams, kg, mL, L — as with the bread recipe), that stays primary as-is, and the site computes a US-customary secondary where possible.
- Count-based units (cloves, fillets, slices, pinch, sprig, bunch, can) are never converted — they're not a measure of volume or weight.
- Servings scaling (§8) scales both the metric and US numbers together, so they always stay consistent with each other.

**How the conversion works, and its honest limits:**
- Pure unit conversions (cup/tbsp/tsp → mL, oz/lb → g) are exact, defined US customary conversions — always reliable regardless of ingredient.
- Converting a *volume* to a *weight* (e.g., "1 cup flour" → grams) requires knowing that ingredient's density. `build.py` has a small sourced table of grams-per-US-cup for common ingredients (flour, sugars, butter, cream, honey, oils, salt, cheese, garlic, lemon juice, water, blueberries), from [King Arthur Baking's Ingredient Weight Chart](https://www.kingarthurbaking.com/learn/ingredient-weight-chart) (retrieved 2026-07-15), plus water's physical density.
- If an ingredient isn't in that table (e.g., "2 tablespoons capers," fresh herbs, produce not listed), Claude does **not** guess a weight — the site instead shows the exact volume-to-volume conversion (mL) as the metric figure, which is always valid math, never a density guess. Nothing is ever fabricated to force a gram value.
- To extend the density table (add an ingredient), edit the `DENSITY_G_PER_CUP` list near the top of `_build/build.py` — keep more specific keywords (e.g. "brown sugar") ahead of generic ones (e.g. "sugar") since the first match wins, and cite the source of any new density value in the surrounding comment.
- Oven temperatures follow the same Celsius-primary principle automatically — see §5c below.

## 5c. Oven temperatures — Celsius primary, Fahrenheit secondary

Same principle as §5b, applied to oven temperatures: the site shows **Celsius first, Fahrenheit second in parentheses** — e.g. "Preheat the oven to 204°C (400°F)." This is also an automated build-time conversion (not something Claude or you need to write by hand), implemented in `_build/build.py` alongside the ingredient conversion.

**How it works:** `build.py` scans the Instructions, Cook's Notes, and Description text of every recipe for temperature mentions — recognizing forms like `400°F`, `400 F`, `400 degrees F`, `400 degrees Fahrenheit`, and the Celsius equivalents — and rewrites each one as `{Celsius}°C ({Fahrenheit}°F)` using the exact conversion (°C = (°F − 32) × 5/9, °F = °C × 9/5 + 32). If a source already writes a temperature both ways (e.g. "220°C (425°F)"), it's left untouched rather than double-converted.

**Limits:** this only recognizes temperatures written in one of the patterns above — highly unusual phrasing could slip through unconverted, in which case Claude should convert it by hand using the same formula and format when writing or completing a recipe. As with ingredient units (§5b), the source `.md` file keeps whatever phrasing was originally used; only the generated `index.html` shows the dual-unit form.


## 6. Workflow — adding a recipe from a URL

1. Fetch the URL. If it can't be retrieved (blocked, JS-rendered, paywalled), say so plainly rather than guessing at the content — flag it as unverified (tag `UNVERIFIED`) and ask the user for the text or a screenshot instead of inventing quantities or steps.
2. Extract, verbatim where possible: title, author, servings, prep/cook/total time, ingredients (with quantities, in whatever unit the source used — don't convert by hand, see §5b), numbered instructions, and any tips explicitly stated by the source.
3. Do not invent nutrition info, difficulty ratings, or tips the source didn't provide — leave the field blank or omit it rather than guessing.
4. Assign a category (existing folder if it fits, new folder if not) and 3–6 tags.
5. **Capture and verify the photo** (mandatory, not optional): extract the source's `og:image`/hero photo and sanity-check it against the dish per §7b before setting `image_local`/`image_source_url`. If it fails the check, is blocked, or genuinely isn't available, leave the image fields empty and note why in `## Missing Information` — don't skip this step silently.
6. Populate the schema in §5, save to `recipes/{category}/{name}.md`.
7. Always keep the `source_url` — this is the citation for every factual claim in the file.
8. **Rebuild the site:** run `python3 _build/build.py` (Claude does this automatically after adding/editing any recipe). It re-scans every file under `recipes/` and regenerates `index.html` in a few seconds — no manual HTML/CSS/JS editing, ever, for a routine recipe addition. Check the console output for the "recipe(s) still have no photo of their own" report (§7b) and the YAML warnings list.

## 6b. Workflow — completing a partial recipe with new information

When a recipe is flagged incomplete (carries the `UNVERIFIED` tag), you don't have to re-supply the whole thing to fix it — just paste whatever you have and Claude merges it in.

**Trigger:** anything like "complete the bread recipe: bake at 220°C for 22–25 min, proof 45 min covered, 3 folds 10 min apart" or "here's the missing info for [recipe]: {paste}". If you're not sure what's missing, open the recipe on the site — the incomplete banner and the missing-info checklist now live at the *bottom* of the page, below the Print Recipe button, listing exactly what's needed (from that recipe's `## Missing Information` checklist). Every recipe page also has a **"Fix or complete this recipe"** box at the very bottom with two shortcuts that need no typing: **"Open recipe file (.md)"** opens the source Markdown file directly (useful for manual edits or copy-pasting into another tool), and **"Copy prompt to paste in chat"** copies a ready-made message — pre-filled with the recipe's file path and title, and phrased as a missing-info request for incomplete recipes or a general correction request for complete ones — straight to the clipboard so you can paste it here with just the details filled in.

**Steps Claude follows:**
1. Identify the target file from the recipe name/slug (asks which recipe if more than one is incomplete and it's ambiguous).
2. Reads that recipe's `## Missing Information` checklist to know exactly what's being supplied.
3. Merges only what the new information covers — times, temps, quantities, steps — into the right sections and frontmatter fields, leaving everything else untouched. User-provided specifics always override previously calculated/inferred values. Quantities are recorded in whatever unit you provide them in — the site converts to metric/US automatically per §5b, no manual conversion needed either way.
4. Updates `## Missing Information`, removing anything now resolved; deletes the section entirely once nothing remains.
5. Once ingredients (with quantities), ordered instructions, and timing are all present, removes the `UNVERIFIED` tag and the "incomplete" banner heading — the recipe graduates to complete.
6. Notes in `## Source` that this update came from user-provided information, dated.
7. Rebuilds the site (`python3 _build/build.py`).

This keeps completing a recipe additive and incremental — one missing detail at a time, never a full re-paste.

## 6c. Workflow — duplicate detection (mandatory before writing any new recipe file)

This project has hit real duplicates twice: two "Spaghetti Carbonara" files and two "Shrimp Scampi" files were created from the same source blog (gamintraveler.com), each republished under a different date-path URL with near-identical text. Exact-URL matching alone doesn't catch this, so duplicate detection is now a required step — for a single recipe add **and** for every URL in a batch import (§6d) — before any new recipe file is written, not after.

**Step 1 — exact source URL match.** Before writing, grep every existing recipe's `source_url` field for the candidate URL. An exact match means this recipe is already in the cookbook — skip it, don't write a second copy.

**Step 2 — same-site-and-title fuzzy match (catches republished/re-dated articles).** Many recipe blogs (this project has seen it specifically from gamintraveler.com and 30seconds.com) republish the same article under a new date path or tip ID, so the URL differs but the content doesn't. Before writing, compare the candidate's domain + normalized title (lowercase, punctuation stripped) against every existing recipe's `source_url` domain + `source_title`/`title`. Treat it as a likely duplicate if the domain matches **and** the titles are the same or near-identical (ignoring minor wording differences like "Authentic" vs. no qualifier). **For 30seconds.com specifically, match on the numeric tip ID in the URL path** (e.g. `30seconds.com/food/tip/38655/...`) rather than the slug text after it — the site republishes the same tip under a slightly reworded slug (e.g. "...Eat All Week..." vs "...Eat This Week...") while keeping the same numeric ID, which a pure title-string comparison can miss (caught during batch 2 of the Flipboard import, 2026-07-16).

**Step 3 — when a likely duplicate is found.** Do not create a second file. Instead:
- If the new source has no additional detail (times, quantities, tips) beyond what's already recorded: skip entirely, and just add the new URL to the existing file's `## Source` section as an "also republished at" line, so the provenance is complete without a duplicate file.
- If the new source fills in something the existing file was missing (e.g. an oven temperature the first source never gave): merge that detail into the existing file per §6b, rather than creating a new file.
- Never keep two files for what is materially the same recipe just because the URLs differ.

**Step 4 — for batch imports specifically (§6d):** run steps 1–2 against the full existing `recipes/**/*.md` set once per URL, before dispatching to a parallel sub-agent, or instruct each sub-agent to do this check itself before writing. Note any skipped-as-duplicate URLs in that batch's report file (`_build/flipboard-batch-N-report.md`) with which existing file they duplicate.

## 6d. Workflow — batch importing from a Flipboard (or similar curated-links) magazine

Used when the source isn't one recipe but a large saved-links collection (e.g. a Flipboard magazine with thousands of stories). Established during the first import from [Food & Flavors](https://flipboard.com/@enetoe/food-flavors-acbn0akgy) (7,729 stories at the time), run in batches of 100, newest-first.

1. **Collect the batch's URLs.** Flipboard's feed is JS-rendered and infinite-scroll, so a plain fetch only returns a page shell — open it with Claude in Chrome, scroll to load stories, and extract each card's real source URL (Flipboard wraps links in a `flipboard.com/redirect?url=...` param — decode that, don't keep the redirect link) plus its displayed title, via a small in-page script rather than reading the accessibility tree card-by-card (much faster at this volume).
2. **Run duplicate detection (§6c) on every URL before converting anything** — against both the cookbook's existing recipes and against other URLs already collected in this same batch (blogs like gamintraveler.com and 30seconds.com resurface the same article multiple times in one feed).
3. **Classify each remaining URL:** single recipe (convert), roundup/listicle/"best of" collection (skip — do not fabricate a recipe from a list of many, and do not follow the links inside it in this pass), or non-recipe/informational article (skip). Record the reason for every skip.
4. **Convert at scale via parallel sub-agents.** Split the batch's single-recipe URLs into chunks (16 URLs per agent worked well) and dispatch general-purpose agents in parallel, each given: the exact schema (§5), the naming convention (§4), the anti-fabrication rule (§6 step 3), the mandatory photo-capture-and-verification step (§6 step 5 / §7b), and an instruction to check for existing files before writing (§6c). Agents only write recipe `.md` files — never README.md, index.html, or run the build script, to avoid race conditions across parallel agents.
5. **After all chunks finish:** rebuild the site once (`python3 _build/build.py`), fix any YAML errors it surfaces (the most common one so far: a `source_title` containing an unescaped colon — wrap it in quotes), check the build's "recipe(s) still have no photo of their own" report (§7b) against the batch and follow up on any that look surprising, update `README.md`'s recipe index, and write `_build/flipboard-batch-N-report.md` listing every write and every skip with its reason (including any photo rejected by the §7b sanity check and why).
6. **Track progress across sessions** in `_build/flipboard-import-progress.md` — which batch number is done, how many stories the source had at last check, and the next batch's starting URLs (collected during the previous batch's scroll, so resuming doesn't require re-scrolling from zero).

## 7. Photo handling

Requested feature: use original photos when available. In practice this has one important constraint — **recipe photos on other people's websites are copyrighted**. Guidance:
- Personal, private, non-redistributed use (this folder, for your own cooking) is low-risk.
- Don't publish this folder publicly, post the images elsewhere, or use them commercially — that would need the original site's permission.
- If Claude's sandboxed environment can reach the image host, it downloads the photo into `images/{category}/` and sets `image_local`. If the host is blocked by the sandbox's network allowlist (this happened with `media.30seconds.com`), Claude sets `image_source_url` instead — the site displays it by loading it live from the source when your browser has internet access, and falls back to a colored initials tile if the image fails to load.
- If you upload/attach your own photo of a dish, that has no copyright complication — always prefer that when you have it.

**Fallback photo for recipes with no image yet (including ones "needing a source"):** every card in the catalog grid and every recipe's detail banner should show a picture rather than a blank initials tile, even for a recipe still tagged `UNVERIFIED`. `build.py` handles this automatically at build time — if a recipe has no `image_local`/`image_source_url` of its own, it borrows the photo from another recipe **in the same category only** (e.g. another sauce for a sauce) and sets `image_is_fallback: true` plus `image_fallback_title` on that recipe's build data. The site labels this honestly with a small overlay caption ("Photo from a similar recipe: {title}") on both the card thumbnail and the detail-page banner — it's never presented as an actual photo of that specific dish, only as a stand-in until a real photo is added. If no recipe in the same category has a real photo either, the recipe shows the plain colored-initials tile instead of a photo — **never a cross-category photo.** Nothing is written back to the recipe's `.md` file for this; it's purely a display-time substitution, recomputed on every build. Once a recipe gets its own real photo, the fallback stops applying to it automatically.

## 7b. Guardrail — verifying a photo actually matches its recipe (incident: 2026-07-16)

**What went wrong:** an earlier version of the fallback rule above borrowed a photo from *any* recipe cookbook-wide when a category had no photographed peer. This produced a genuinely wrong result — "Richard and Suzanne's Famous Spaghetti Sauce" (category `sauces`, the only recipe in that category) displayed a photo of "Crispy Potato Cheese Croquettes" (category `appetizers`), because that happened to be the first recipe in the dataset with any photo at all. A caption doesn't fix a wrong photo — it was still showing an unrelated dish. Fixed by restricting the fallback to same-category only (§7).

**A second, subtler version of the same risk, found while backfilling photos for this incident:** even a source site's own `og:image` isn't automatically trustworthy. `recipes/seafood-mains/bacalao-a-la-vizcaina.md`'s source article (gamintraveler.com) has its `og:image` and every in-article image filed under `Salmorejo-*.jpg` — a completely different, unrelated Spanish dish (a cold tomato soup, not a cod stew). The source site itself has mismatched images on that article. This was caught by checking the image filename/URL against the dish name before using it, and the recipe was deliberately left without `image_source_url` (documented in its `## Missing Information`) rather than propagating the wrong photo just because it came from the "official" source.

**Guardrail — mandatory before setting `image_local` or `image_source_url` on any recipe, whether adding one or backfilling one that's missing a photo:**
1. Extract the candidate image (the source page's `og:image` / `twitter:image` meta tag is the most reliable single field; fall back to the largest/first image inside the article body if there's no `og:image`).
2. **Sanity-check it before using it** — does the image filename/URL, alt text, or surrounding context plausibly match the recipe's actual dish (main ingredient, dish name, or a close synonym)? A generic camera filename (e.g. `MG_0607.jpg`) from the *correct* article page is fine; an image path naming a *different, specific dish* is a red flag and should not be used, even if it's technically the page's designated `og:image`.
3. If the check fails or is inconclusive, do not set the image field — leave it unset, add a line to `## Missing Information` explaining what was found and why it wasn't used, and let the same-category fallback (§7) or the plain initials tile take over. Never guess or force a plausible-looking photo through.
4. This check applies per-recipe during normal adds (§6), during backfills, and per-URL during batch imports (§6d) — the same discipline as the duplicate-detection check in §6c, and for the same reason: a wrong-looking-right answer is worse than an honest "not available yet."
5. `build.py` also prints a build-time report of every recipe still missing its own real photo (same-category fallback or no photo at all) after every build — check this output after adding recipes so gaps don't go unnoticed.

## 8. Workflow — portion scaling

Two ways this happens:
- **In chat:** "make the salmon for 6 people" (written for 4) → Claude multiplies each parsed ingredient quantity by `target_servings / servings`, rounds to sensible cooking units, and presents the scaled list without overwriting the file unless asked to.
- **In the browser:** every recipe page has a servings +/- stepper that rescales every ingredient live, client-side, using the same math — no chat round-trip needed once the site is open.

## 9. Workflow — search by ingredient / tag

- **In chat:** "What can I make with peaches?" → Claude searches `recipes/**/*.md` ingredient sections and tags directly (always current, no index file needed).
- **In the browser:** the search bar at the top of `index.html` filters the live recipe grid by title, category, cuisine, tags, diet, and ingredient text as you type — same data, instant, no server required. Typing a search term while a recipe's detail page is open automatically returns you to the browse grid so the results are visible (the same behavior as clicking a sidebar category from a detail page).

## 10. Workflow — shopping list generation

Two ways this happens, and they're deliberately independent — use whichever fits the moment:

**In chat (a saved file):** "Make a shopping list for the salad and the salmon" → Claude reads the named recipes' Ingredients sections, combines duplicate ingredients (adding quantities where units match, listing separately where they don't), groups by rough grocery-aisle category (produce, dairy/eggs, meat/seafood, pantry, herbs/spices, other), and writes a new file to `shopping-lists/{date}-shopping-list.md`. Scaled quantities (§8) are used if a different serving count was specified.

**In the browser (no chat needed):** every recipe detail page has a **"+ Add to Shopping List"** button above the ingredients, which adds that recipe's ingredients (at whatever serving count the page is currently showing) to a running list. A **Shopping List** button in the header (with a count badge) opens that list. There:
- A **"By Aisle" / "By Recipe" toggle** at the top switches how the list is grouped, on-screen and in Print/Copy alike (the toggle choice is remembered across reloads, same as the list itself). **By Aisle is the default** — items are organized into grocery-store sections (Produce, Meat & Seafood, Dairy & Eggs, Bread & Bakery, Frozen, Condiments/Oils & Sauces, Herbs & Spices, Pantry & Dry Goods, Beverages, Other) so a trip through the store, or an online-cart session, only has to touch each section once. Every item still carries a small recipe-name tag so it stays traceable to its source. **By Recipe** is the original grouped-by-recipe view, unchanged.
- Aisle assignment is a **client-side keyword lookup** (`AISLE_KEYWORDS` in `_build/template.html`) — the same "small, documented, ordered, most-specific-phrase-first, first-match-wins" pattern as the ingredient-density table in §5b, applied for the same reason: this is a shopping-order convenience, not a factual claim about any product. A misclassified ingredient is never hidden, just filed under the wrong (or "Other") section — the on-screen note calls this out, and nothing here is presented as authoritative. To extend or correct it, add a `[phrase, aisle]` pair to `AISLE_KEYWORDS`: specific compounds (e.g. `"chicken broth"`) must be listed before the generic word they contain (e.g. `"chicken"`) or the generic entry wins first, exactly like the density table's ingredient-keyword ordering rule.
- In either grouping mode, ingredients are never merged into one combined total — the same-sounding ingredient can mean different things across recipes (bread flour vs. all-purpose, lemon juice by volume vs. by fruit), so auto-merging risked silently showing a wrong combined amount. Keeping every line traceable to its recipe (via a card heading in Recipe mode, or a small tag in Aisle mode) is what's consistent with this project's no-fabrication rule.
- Each ingredient has a checkbox to tick off while shopping (struck through when checked); in Recipe mode a "Remove recipe" link drops that recipe's items; "Clear list" empties everything regardless of grouping mode.
- **Print list** opens the browser print dialog. Rather than CSS-hiding pieces of the on-screen grouped view (which turned out not to fully suppress the recipe cards/headings and the sidebar on the first page in practice — a `@media (max-width:860px)` mobile-layout rule was winning the cascade at print widths and re-showing the sidebar, fixed with `!important`), the print output is built by JS as an **entirely separate, dedicated flat DOM block** — a "Shopping List" heading, then one continuous checklist with no sidebar, no header, no toolbar, and no card boxes — kept hidden on-screen and shown only via `@media print`, scoped so it only appears while the shopping-list route is actually active (so printing a recipe page is never affected). It mirrors whichever grouping mode is currently active: a plain-text label (bold, no box, no button, no "Remove recipe" link) directly above each aisle's or recipe's items, so everything stays identifiable without any on-screen card styling. **Copy to clipboard** copies that same grouped content as plain text (section/recipe name line, then `- ` bulleted ingredient lines — in Aisle mode each line also ends with `(Recipe Name)` since there's no heading grouping by recipe — blank line, next section) for pasting straight into Word, Notes, a messaging app, or a grocery app.
- The list (and the grouping-mode toggle) are saved to the browser's local storage keyed to this file, so they persist across reloads in the same browser. This is a reasonable-effort convenience, not a guarantee — some browsers restrict local storage for files opened directly (`file://`) rather than through a server, in which case everything still works fully but resets when the page is closed. Nothing here touches the recipe `.md` files or requires a rebuild.

## 10b. Workflow — favoriting recipes

Entirely in-browser, no chat round-trip, no file written — same pattern as the shopping list (§10).

- Click the **star icon** on any recipe card (top-left of its photo/initials tile) to favorite it without opening the recipe, or click **★ Add to Favorites** in the title bar of a recipe's detail page. The star fills gold (card) or the button turns gold (detail page) once favorited; click again to remove it.
- Click **★ Favorites** at the top of the sidebar (right under "All Recipes") to browse only your favorited recipes — it behaves exactly like a category filter, including working together with the search bar, and shows a live count of how many recipes are currently favorited.
- Favorites are saved to the browser's local storage keyed to this file, so they persist across reloads in the same browser — the same reasonable-effort persistence and the same file:// caveat as the shopping list (§10). Favoriting never touches the recipe `.md` files or requires a rebuild.

## 11. Workflow — editing & notes

"Add a note to the salmon recipe that I used less cream" → Claude edits only the `## My Notes` section of that file, appending with a date stamp, leaves the rest untouched, then reruns the build (§6, step 7) so the site reflects it. Any other edit (fixing an ingredient, adding a step) is a direct edit to the relevant section, confirmed in one line, followed by the same rebuild.

## 12. The standalone HTML site — architecture and design

`index.html` is a **single self-contained file**: all CSS and JS are inline, and every recipe's data is embedded directly in the page as JSON (not fetched from a separate file), so it opens and works fully offline just by double-clicking it — no server, no build tool needed to *view* it. Recipe photos are the one exception: those load live from their source URL (or your local `images/` copy) when your browser has internet access.

**How incremental addition works without "recompiling" the app:** the design/CSS/JS in `_build/template.html` never changes when you add a recipe — only the embedded data does. Adding recipe #4, #40, or #400 is the same two-step process: (1) write/update a Markdown file under `recipes/`, (2) run `python3 _build/build.py`, which re-embeds the full current dataset into a fresh `index.html` in under a second. You're never hand-editing HTML, and the "app" itself (search, filters, detail view, servings scaler) is written once and reused for every recipe automatically.

**Theme:** Botanical Garden (fern green `#4a7c59`, marigold `#f9a620`, terracotta `#b7472a`, cream `#f5f3ed`; serif headers, sans body; base font size 18px) — chosen from the theme-factory skill's curated set, picked for its explicit "food presentations, farm-to-table content" fit. To change themes later, ask Claude to restyle `_build/template.html` with a different theme-factory palette and rebuild.

**Features implemented:** live search-as-you-type (title/ingredient/tag/category) that always searches the full recipe library — the two filter directions are symmetric: clicking a sidebar category always clears any active search term (so a keyword typed earlier can never hide that category's recipes), and typing a search keyword always switches the active filter back to "All Recipes" (so a category or ★ Favorites filter can never silently hide search matches outside that group); a ★ Favorites filter with per-recipe star toggles on both the card grid and the detail page (§10b), responsive recipe-card grid, a detail page per recipe (hash-routed, so it's linkable/bookmarkable — `index.html#recipe/{slug}`), a live servings scaler with fraction-aware quantity formatting, a grid-aligned ingredient list (quantity, secondary quantity, and name always line up in fixed columns instead of wrapping unpredictably), an in-browser shopping list with a By Aisle/By Recipe grouping toggle and matching print/copy support (§10), a print button with print-specific CSS, and a "Fix or complete this recipe" box at the bottom of every recipe page (§6b).

**Recipe detail page layout:** the description sits at the very top of the page, directly under the photo banner, with a compact stat box in the top-left corner listing Prep / Cook / Total time and a three-level Difficulty icon (Easy/Moderate/Hard, or "N.A." for any of the four facts that's missing rather than silently omitting it) — see §5's difficulty-normalization note. The source link sits directly below the description and is always a clickable URL when one is on file ("N.A. (not recorded)" otherwise). The incomplete-recipe warning banner and the "still needed" checklist (§6b) are shown at the *bottom* of the page, below the Print Recipe button, so they don't push the actual recipe content down. Every card and every detail banner always shows a photo — including recipes still tagged `UNVERIFIED` — via the fallback-photo mechanism described in §7.

**On Claude Design specifically:** Anthropic does have a product called Claude Design — an Anthropic Labs tool (Claude Opus 4.7-powered, research preview for Pro/Max/Team/Enterprise) for building polished visual work like prototypes, decks, and branded UIs from a design system ([Anthropic announcement](https://www.anthropic.com/news/claude-design-anthropic-labs), [Claude Help Center](https://support.claude.com/en/articles/14604416-get-started-with-claude-design)). It's built for teams building repeatable, on-brand visual output. The site described above already meets "large text, uncluttered, professional, photo-forward" without it. Claude Design would make more sense if this became a shareable, multi-user, brand-managed cookbook site later.

## 13. Maintenance rules

- Never change the schema in §5 without updating this file first, and without updating `_build/build.py`'s parser to match — consistency across all recipes is what makes search/scaling/shopping-lists/the HTML site all work.
- Never hand-edit `index.html` — edit `_build/template.html` (design/behavior) or a recipe's `.md` file (content), then rebuild.
- Every new category gets a matching folder in both `recipes/` and `images/`.
- If a source can't be verified (broken link, empty fetch, paywall), the recipe file should say so explicitly (tag `UNVERIFIED`) rather than presenting placeholder content as fact.
- **A note on this OneDrive folder specifically:** edits made through file-editing tools can occasionally sync to this folder's on-disk copy with a short delay. If a rebuild ever throws a syntax error immediately after an edit to `_build/build.py` or `_build/template.html`, wait a few seconds and rerun `python3 _build/build.py` before assuming something is actually broken. The same delay has been observed on plain Markdown files (this meta-prompt and `README.md` included) — after any edit to a `.md` file, re-read the on-disk copy before relying on it being complete, and if it looks cut off, rewrite it directly rather than assuming the edit failed.
- **A stronger version of the same issue, hit while building the favorites feature (2026-07-16):** after several rapid `Edit` calls to `_build/template.html` in one conversation, the sandbox's shell (`bash`) kept reading a stale, truncated copy of that file for multiple minutes — long enough that "wait a few seconds and retry" wasn't enough, even though the file-editing tool's own `Read` of the exact same path showed the correct, complete file the whole time. Symptom: `python3 _build/build.py` reports success ("Built ... N recipe(s)...") but the resulting `index.html` is truncated mid-file (check with `tail -c 300 index.html` — it should end in `</script>\n</body>\n</html>`, not mid-sentence). If this happens: `Read` the full `_build/template.html` with the file-editing tool (not the shell) to get the known-good version, `Write` it to a path outside this OneDrive-mounted folder (e.g. the session's scratch/outputs directory), then run `build.py` with `TEMPLATE_PATH` (and if needed `OUTPUT_PATH`) temporarily pointed at that scratch copy instead of trusting the shell's view of `_build/template.html` directly. Recipe `.md` files under `recipes/` have not shown this problem (each is small and typically edited once per session, not repeatedly), only the much-larger, repeatedly-edited `template.html`.
- **The same staleness bug also hit `_build/build.py` itself (batch 2 of the Flipboard import, 2026-07-16)** — after many parallel sub-agents wrote dozens of new recipe files in one session, running `python3 _build/build.py` from the shell threw a `SyntaxError` ("unterminated string literal") at a specific line, but the file-editing tool's `Read` of that exact line showed completely valid, correctly-terminated code. This confirms the bug isn't specific to `template.html` — it's a general symptom of the shell's cached view of any `_build/` file lagging behind the true on-disk state after a burst of activity in the same session. Same fix: `Read` the full file with the file-editing tool, `Write` a verified copy to the scratch/outputs directory, then run it from there with `ROOT`/`RECIPES_DIR`/`TEMPLATE_PATH`/`OUTPUT_PATH` overridden to point back at the real project folder as needed. Don't waste time debugging the "syntax error" itself when this happens — cross-check the shell's view against a fresh `Read` first.
