# Flipboard import — batch 1 report

Source magazine: [Food & Flavors](https://flipboard.com/@enetoe/food-flavors-acbn0akgy) (@enetoe on Flipboard). The magazine showed **7,729 stories** total when this batch was collected (2026-07-16), newest first. At 100 stories per batch, this is roughly batch 1 of ~78.

## What batch 1 covered
The 100 most recent stories in the feed at collection time. Two of those were duplicates of recipes already in this cookbook (the peach/blueberry/cucumber salad and the one-pan salmon), and one was the "13 Hummus Recipes" roundup that's the source of the existing Dips & Spreads collection — all three were skipped as already-present. One more (the bread dough article) was already in the cookbook but flagged incomplete; it's now been completed using a direct page read.

## Result
- **62 new recipe files written** (plus 1 existing recipe completed: One Dough, Four Breads)
- **35 stories skipped** as roundup/non-recipe/failed-fetch — see list below
- **2 near-duplicate pairs merged after the fact** (see "Duplicate cleanup" below) — batch 1 initially produced 64 files across 2 sub-agent chunks that unknowingly picked up two different date-path URLs for the same source articles; these are now 1 file each, and the cookbook's meta-prompt (§6c) was updated with a formal duplicate-detection rule so future batches catch this before writing rather than after
- **17 category folders** now exist under `recipes/` (5 pre-existing: salads, seafood-mains, pasta, breads, dips-spreads; 12 new: poultry, beef, soups, sides, sauces, sauces-dressings, desserts, beverages, breakfast, sandwiches, appetizers, meat-mains)

## Duplicate cleanup (done 2026-07-16, after initial batch 1 completion)
- **Spaghetti Carbonara**: `recipes/pasta/spaghetti-carbonara.md` and `recipes/pasta/roman-style-spaghetti-carbonara.md` were both gamintraveler.com's "The Authentic Spaghetti Carbonara Recipe Italians Actually Use," republished under `2026/04/25` and `2026/01/28` respectively (a third date-path, `2025/09/08`, is queued for batch 2 and is the same article again). Kept the more detailed version (with calorie range and timing notes) at `recipes/pasta/spaghetti-carbonara.md`; the other file was removed and both alternate URLs are now recorded in that file's `## Source` section for provenance.
- **Shrimp Scampi**: `recipes/seafood-mains/shrimp-scampi.md` and `recipes/seafood-mains/buttery-garlic-shrimp-scampi.md` were both gamintraveler.com's "The Shrimp Scampi Recipe That's Buttery, Garlicky, And Ready In Minutes," republished under `2025/08/16` and `2026/04/25`. Kept the version with clearer step labels at `recipes/seafood-mains/shrimp-scampi.md`; the other file was removed and its URL recorded in the kept file's `## Source` section.

## Skipped stories (35) and why
- seriouseats.com — "13 Fast Fried Rice Recipes" — roundup
- immigrantstable.com — "15 Potluck Pasta Salads" — roundup
- eatingwell.com — "One-Pot Gut-Healthy Dinner Recipes" — roundup
- eatingwell.com — "Hydrating Salad Recipes for Summer" — roundup
- foodandwine.com — "Debunk Major Sourdough Myth" — informational, not a recipe
- eatingwell.com — "Gut-Healthy Salad Recipes for Summer" (21 recipes) — roundup
- eatingwell.com — "Meal-Prep 5 Mediterranean Diet Lunches" — roundup
- parade.com — "21 Types of Fish To Eat" — informational, not a recipe
- goodhousekeeping.com (UK) — hummus/tuna salad piece — fetch blocked even with the Chrome fallback
- earthsattractions.com — "7 Foods That Protect Your Memory" — informational, not a recipe
- gamintraveler.com — "Try These Recipes in Vietnam" — roundup
- barbecuebible.com — griddled salmon — technique essay, no formal ingredient list/quantities
- gamintraveler.com — "Try These Dishes Instead" (Spain) — roundup
- thekitchn.com — Giada lemon pasta "I tried it" review — review article, actual recipe hosted at giadzy.com
- ruthybellerecipes.com — "Soups That Warm You Up Fast" — roundup
- aol.com — "10 Best Chicken Salad Recipes" — roundup
- eatingwell.com — "30 Days of Dinners to Lose Visceral Fat" — roundup
- simplyrecipes.com — "Top 10 Salmon Recipes" — roundup
- thehonoursystem.com — "38 Winter Soups" — roundup
- gamintraveler.com — "Most Delicious Stews Around the World" — roundup
- littlebitrecipes.com — "Seafood Recipes Bursting With Flavor" (30 recipes) — roundup
- apartmenttherapy.com — bolognese review — review article, recipe hosted at thekitchn.com
- ketocookingchristian.com — "32 Keto Seafood Dinners" — roundup
- immigrantstable.com — "21 Holiday Salads" — roundup
- ruthybellerecipes.com — "12 Dinners So Fast" — roundup
- littlebitrecipes.com — "Meals for Two" (30 recipes) — roundup
- alwaysusebutter.com — "24 Casseroles" — roundup
- eatingwell.com — "Healthy Lemonade Recipes" (11 recipes) — roundup
- aol.com — professional baker no-bake piece — review article, no ingredient quantities
- immigrantstable.com — "17 Vintage Dishes We Stopped Making" — roundup
- immigrantstable.com — "19 Vintage Recipes" — roundup
- littlebitrecipes.com — "Easy Skillet Dinners" (54 recipes) — roundup
- eatingwell.com — Ina Garten cauliflower toast piece — narrative essay, no ingredient list/quantities
- simplyrecipes.com — Top 10 salmon (duplicate mention, see above)

## Data-quality notes
- Every written recipe carries `date_added`/`retrieved_date` of 2026-07-16.
- Recipes where the source didn't state a time, servings count, or difficulty were left blank in the YAML (never guessed), tagged `UNVERIFIED`, and given a "Missing Information" checklist — the site shows a warning banner on these. Most of batch 1 is flagged this way because many of the source blogs (especially gamintraveler.com and 30seconds.com) write servings/time as vague ranges or omit them.
- Two pairs of near-duplicate recipes exist (two "Spaghetti Carbonara" files, two "Shrimp Scampi" files) because the Flipboard feed contained two separate flips of the same source blog on different dates. Both were kept as separate files rather than assumed identical, since the fetched text differed slightly between the two page loads.
- Two files (`gambas-al-ajillo.md`, `marmitako-basque-tuna-potato-stew.md`) initially failed the site build due to an unescaped colon in `source_title` (a YAML syntax issue, not a content issue) — fixed by quoting those values.

## Next batch
Items 101–111 of the originally-collected 111 are already queued (see `flipboard-batch-1-queue.json` in the working outputs, held for batch 2) — say "convert the next batch" to continue, which will re-open the magazine and continue scrolling past story 100.
