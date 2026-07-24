# Flipboard import — Batch 8 report

**Date:** 2026-07-24
**Result:** 332 → 348 recipes (**16 written**). Target was ~20 (a deliberately smaller "quick" batch).
**Source magazine:** [Food & Flavors](https://flipboard.com/@enetoe/food-flavors-acbn0akgy) (@enetoe)

## Funnel
- **91 unique candidate URLs** collected in one scroll session (~30 scroll actions, `scroll_amount: 8`, ~3s waits — the router-safe cadence established in batch 7). The feed restarted from the top as always and reached cards dated back to roughly **June 2024**.
- **Duplicate/roundup filtering (pre-conversion):** 48 exact-URL or 30seconds tip-ID duplicates against the existing 332 recipes, and 21 roundups/listicles. Left **22 single-recipe candidates**.
- **22 dispatched/converted** → **16 written**, **6 not written** (2 no-recipe reviews + 4 same-dish duplicates the URL-level check missed — see below).

## Written (16)
| Recipe | Category | Source | Notes |
|---|---|---|---|
| Sauteed Spinach & Kale | sides | 30seconds.com (tip 74950) | |
| Lemon Turmeric Broccoli | sides | 30seconds.com (tip 41459) | distinct from existing `turmeric-baked-broccoli` (tip 65719) — different recipe |
| Fermented Garlic With Honey | sauces | 30seconds.com (tip 73908) | |
| Bourbon Chocolate Derby Pie | desserts | 30seconds.com (tip 19956) | |
| Peanut Butter Spider Cookies | desserts | xoxobella.com | fetched via Chrome (raw fetch returned a shell) |
| No-Knead Olive Cheese Bread | breads | tastingtable.com | |
| Avocado Cilantro Dressing | sauces-dressings | thehonoursystem.com | page canonicalizes to `creamy-cilantro-lime-dressing…`; kept the requested URL |
| Caipirinha | beverages | 2foodtrippers.com | fetched via Chrome (shell) |
| Brazilian Lemonade | beverages | chowhound.com | **UNVERIFIED** — source is a prose guide, no quantities/servings/times |
| Baked Bananas in Brown Sugar | desserts | tastingtable.com | **UNVERIFIED** — technique article, no quantities/servings |
| Banana Bread Crumb Cake | desserts | xoxobella.com | no structured time/servings on source card |
| Chicken Thigh Marsala | poultry | xoxobella.com | no structured time/servings on source card |
| Garlic Steamed Clams | seafood-mains | orwhateveryoudo.com | |
| Batata Rosti com Carne-Seca | meat-mains | receitas.globo.com | fetched via Chrome; steps restructured/translated (no verbatim reproduction) |
| Pan-Seared Rib-Eye With Mushroom-Hunter's Sauce | beef | southernliving.com | fetched via Chrome |
| Lemon-Blueberry Trifle | desserts | eatingwell.com | fetched via Chrome |

## Not written (6)

### 2 reviews with no real recipe
- **Kate Middleton Watermelon Salad** (thekitchn.com) — "I tried it" review; the actual recipe (quantities/steps) lives on womenshealthmag.com. No ingredient list with amounts.
- **4-Ingredient Gnocchi Skillet** (cubbyathome.com) — syndicated review of a Kitchn recipe; prose only, no quantities or numbered steps.

### 4 same-dish duplicates the URL/tip-ID check missed
The pre-conversion dedup compares exact `source_url` and 30seconds tip IDs. It does **not** catch the same dish published on a **different domain** or the same gamintraveler article **re-dated under a new URL path**. Four slipped through and were caught only *after* the build, by a dish-name/slug cross-check against the existing library:
- **bacalhau-a-bras** — my gamintraveler version (`2024/08/23`) overwrote the existing file (already in the cookbook from **2foodtrippers.com**, retrieved 2026-07-17). Original **restored**; the gamintraveler link was added to it as an "also published at" citation.
- **pasta-alla-norma** — the xoxobella candidate (#52) overwrote the existing file (already in from **gamintraveler `2026/05/01`**). Original **restored**; xoxobella added as an "also published at" citation.
- **cheese bread** (gamintraveler `2024/05/17`) — same article as the existing `breads/cheese-bread.md` (gamintraveler `2025/10/03`, the classic gamintraveler re-date pattern). New file **deleted**; alt URL noted on the existing file.
- **sancocho** (gamintraveler `2024/08/04`) — same article as the existing `soups/traditional-colombian-sancocho.md` (gamintraveler `2026/05/29`). New file **deleted** (the existing file already documented the `2024/08/04` redirect).

**Two of the four (bacalhau, pasta-norma) produced identical filenames and so silently overwrote the originals** — caught because the post-build recipe count rose by only 18 instead of 20, then confirmed by cloning the live repo and diffing. The originals were recovered from the repo clone; no data was lost. The other two (cheese bread, sancocho) had *different* slugs and were caught by a keyword cross-check of every new dish name against all existing titles.

## Lessons / how to apply next time
1. **Add a post-build dish-name cross-check, not just URL/tip-ID dedup.** For every gamintraveler, xoxobella, and 30seconds candidate, compare the dish name against existing titles before (or immediately after) writing — the URL check alone missed 4/22 this batch. gamintraveler in particular re-publishes the same article under new `YYYY/MM/DD` path segments, so its URLs are unreliable as dedup keys.
2. **Watch the recipe-count delta after building.** If `find recipes -name '*.md' | wc -l` doesn't increase by exactly the number of files written, some writes overwrote existing recipes (identical slug). Clone the live repo and `git status`/`git diff` to see exactly which files are new vs. modified vs. clobbered before publishing.
3. Browser-fallback domains behaved as documented — gamintraveler, receitas.globo.com, southernliving.com and eatingwell.com all fetched cleanly via Claude-in-Chrome `navigate` + `get_page_text` where raw `web_fetch` returned a shell or was blocked.
4. Yield note: 16/22 written (73% of dispatched candidates; 4 dups + 2 non-recipes removed). Continue expecting heavy overlap in the newer (post-2024) range of this magazine.
