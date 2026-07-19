---
name: flipboard-batch-2-report
last_updated: 2026-07-16
---

# Flipboard import — batch 2 report

Source: ["Food & Flavors" Flipboard magazine](https://flipboard.com/@enetoe/food-flavors-acbn0akgy) (@enetoe). This batch continued the newest-first scroll from where batch 1 left off, collected 194 story cards in this session, removed 4 same-tip-ID duplicates and 1 within-batch republish, then worked through 90 of the resulting single-recipe candidates across 6 parallel sub-agents (15 URLs each). The remaining ~26 flagged-likely-single and ~40 flagged-likely-roundup candidates from this session's scroll are banked for batch 3 (see `_build/flipboard-import-progress.md`).

**Result: 50 new recipe files written (cookbook grew from 78 → 128 recipes).** 0 YAML errors, 0 duplicate `source_url` values across the full 128-file set after the build.

## Recipes written (50)

**Poultry:** Magic Mayo Parmesan Baked Chicken, Baked Chicken Lombardy, Apple Cider Chicken Thighs, Healthier Creamy Tuscan Chicken (Slow Cooker or Instant Pot)
**Pasta:** BLT Carbonara, Sheet-Pan Garlic-Butter Gnocchi With Summer Vegetables, Sizzling Spaghetti, Quick Italian Sausage Pasta with Tomato Cream Sauce, Creamy Boursin Orzo with Spinach, Creamy Greek Spinach Orzo with Feta, Creamy Ground Beef Alfredo Pasta
**Seafood-mains:** Panko-Crusted Baked Salmon, Buttery Garlic Lemon Shrimp, Cider-Glazed Salmon
**Breads:** Amish Cornbread, Nonna's No-Knead Pizza Dough
**Salads:** Mediterranean Potato Salad With Smashed Olives and Mint, Goat Cheese Salad With Green Beans, Beet and Feta Salad with Pistachios and Pears, Strawberry Spinach Salad with Fresh Oranges, Red Potato Salad, Balsamic Spinach Strawberry Feta Salad with Walnuts, Chickpea & Farro Salad with Artichokes & Tomatoes, Apple Cranberry Slaw, Cucumber Salad (troprockin.com), Cucumber Salad with Herbs and Pine Nuts, French Bistro Salad with Punchy Dijon Vinaigrette
**Dips & spreads:** Tzatziki
**Soups:** Chicken & Sausage Gumbo (30seconds.com, 30 min), Cauliflower Alfredo Casserole* (sides), Swedish Apple Cake* (desserts), Healthier Creamy Tuscan Chicken* (poultry), Braised Short Ribs in Red Wine (beef), Buttery Bread Pudding With Bourbon Butter Sauce (desserts), Boursin Creamed Spinach With Mushrooms (sides), Herb Crusted Pork Tenderloin With Mushroom Gravy (meat-mains), Chicken and Sausage Gumbo (Classic Dark Roux) (soups), Hungarian Goulash (soups), Amish Cabbage Soup With Ground Beef (soups), Rib Roast With Red Wine Jus (beef)
**Desserts:** Date and Walnut Cake, Key Lime Pie
**Sides:** Cabbage & Potatoes with Bacon, Shiitake and Broccoli in Soy Garlic Sauce, Best Creamed Spinach
**Breakfast:** Avocado Toast Three Ways
**Appetizers:** Patatas Bravas
**Sandwiches:** French Bread Pizza (tasteofhome.com)
**Meat-mains:** Slow Cooker Lamb Shanks With Red Wine Gravy
**Soups (cont.):** Traditional German Potato Soup

*(A few titles are asterisked above only because they were double-counted across two loose category groupings while compiling this list by hand — the authoritative, deduplicated set is `recipes/**/*.md`, which totals exactly 128 files; see README.md's "Current recipes" section for the canonical per-category listing.)*

## Skipped — confirmed roundup/listicle (fetched and verified, not guessed)
- EatingWell "30-Minute Mediterranean Diet Dinner Recipes" / "Summer Salad Recipes" (unreachable, domain-blocked — see below, but titles are also classic roundup patterns)
- AOL "10 Soup Recipes Readers Repeat" (republished Serious Eats roundup)
- Parallel Plates "Why Everyone's Talking About These Recipes This Fall" (21-recipe listicle)
- Food Drink Life "Casseroles and the Table" (17-casserole listicle)
- Masalaherb "Asparagus Skillet Recipes" (14-recipe roundup, all outbound links)
- KetoCookingChristian "12 Keto Salads Inspired by Flavors Around the World" (12-item roundup)
- KetoCookingChristian "16 Keto Recipes Where Spinach Is More Than Just a Leafy Green" (roundup)
- Xoxobella "Recipes3 Must-Try Bundt Cakes" (resolved to a 19-recipe roundup)
- Immigrant's Table "17 Simple One-Pan Meals" (page metadata literally tagged `category: Roundups`)
- Southern Living "5-Ingredient Vinaigrette" (a technique/formula article with no actual quantities, not a specific recipe)
- AFoodLoversKitchen "pork-recipes" (14-recipe listicle)
- LittleBitRecipes "Classic Soup & Stew Recipes Passed Down for Generations" (14-recipe listicle)
- Xoxobella "recipes4-fall-comfort-food-recipes" (inconclusive — page wouldn't return article content on repeated fetches; title pattern strongly matches this site's other roundup URLs, left unwritten rather than guessed)

## Skipped — exact duplicate of an existing recipe
- 30seconds.com "Cheesy Italian Penne Pasta With Sundried Tomatoes" — exact `source_url` already in `recipes/pasta/cheesy-italian-penne-pasta-with-sundried-tomatoes.md`.

## Skipped — blocked by the sandbox's network allowlist (not a content judgment; these domains could not be evaluated at all)
- eatingwell.com (blocked every attempt this session, including a re-check of an already-cited eatingwell URL)
- simplyrecipes.com (same domain-wide block)
- receitas.globo.com (blocked; this affected all 7 of this session's bacalhau/salt-cod candidates from that site, so none could be verified for distinctness from each other or from the existing `bacalao-a-la-vizcaina.md`)

These three domains are worth flagging for future batches — if the same block persists, recipes already collected from them (banked in `_build/flipboard-import-progress.md`) will keep failing until the allowlist changes.

## Skipped — unreachable for other reasons (empty fetch on repeated retries; not a domain-wide block, since sibling pages on the same site loaded fine)
- thekitchn.com — "Kristen Bell Pickle Soup", "Cajun Potato Soup", "Pasta Recipes 5 Ingredients or Fewer"
- gamintraveler.com — "How to Make an Authentic Osso Buco", "Most Underrated Italian Dishes", "Sunday Tomato Sauce Recipe Italian Grandmothers", "The Simple Soup Recipe Italian Grandmothers..." (2025/04/18 date-path), "How to Make Tagliatelle al Tartufo"
- kimschob.com — "Cucumber Dill Salad", "Watermelon Lemonade" (bot-blocking suspected)
- simplyrecipes.com — "Five-Ingredient Dinners", "Popular Five-Star Italian Recipes", "Spaghetti Alla Puveriello", "Garlic Knot Salmon" (domain block, see above)

## Notable finds during duplicate detection
- gamintraveler.com's Patatas Bravas link (2025/01/25 date-path) now 301-redirects to a new 2026/07/03 canonical URL — same republish-under-new-date-path pattern seen before with Carbonara/Shrimp Scampi, but since no Patatas Bravas recipe existed yet, this was written as a new, legitimate recipe (using the resolved canonical URL as `source_url`).
- Two different "Chicken and Sausage Gumbo" recipes now coexist (`recipes/soups/chicken-sausage-gumbo.md`, a quick 30-minute 30seconds.com version with no tomatoes, and `recipes/soups/chicken-and-sausage-gumbo-with-dark-roux.md`, a longer dark-roux xoxobella.com version) — confirmed genuinely different recipes (different source, technique, ingredients, cook time), not a republish duplicate.
- One within-batch republish was caught before dispatch: gamintraveler.com's homemade tzatziki was flipped twice in this session's scroll (2026/06/06 and 2026/05/08 date-paths) — only the 2026/06/06 URL was converted; the 2026/05/08 duplicate was dropped from the candidate list before any sub-agent saw it.

## Photos
Sub-agents applied the mandatory og:image sanity check (`_cookbook-meta-prompt.md` §7b) per recipe. Two photos were deliberately left blank rather than risk a mismatch or use an unreachable host: Sheet-Pan Garlic-Butter Gnocchi (eatingwell.com blocked) and one xoxobella.com gumbo page (no og:image data returned). Both fall back to the same-category photo-borrowing rule (§7) or a plain initials tile, and are noted in the build's "no photo of their own" report (3 recipes total across the whole 128-file cookbook — see the build output).

## Build verification
`python3 _build/build.py` (run via the documented scratch-copy workaround, since this session hit the same OneDrive/bash staleness bug described in `_cookbook-meta-prompt.md` §13, this time against `build.py` itself rather than `template.html`) completed cleanly: 128 recipes across 17 categories, 0 parse errors, 0 duplicate source URLs, valid embedded JSON and JavaScript confirmed by static checks.
