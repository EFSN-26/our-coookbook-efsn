---
name: flipboard-batch-7-report
date: 2026-07-21
---

# Flipboard import — Batch 7 report

**Result: 266 → 332 recipes (66 written).** Requested batch size was 50; actual yield was 66, comfortably above target.

## Why yield recovered after batch 6's collapse (11 written)

Batch 6's report flagged that a single scroll session was resurfacing content already covered by batches 1-5 (roughly Dec 2024 and newer), because Flipboard's feed restarts from the top every session and a normal-length scroll doesn't reliably outrun that overlap once the cookbook is a few hundred recipes deep.

Batch 7 scrolled much further in one sitting — over 250 individual scroll actions (`scroll_amount: 8`, ~3s waits, occasional recovery from a transient "Page still loading" error and one client-side-router glitch that briefly broke the page into a "this page does not exist" state after scrolling too aggressively; both resolved by a fresh navigate and slower scrolling) — reaching story dates back to roughly **April 2024**, about four months further back than any prior batch (batch 4, the previous deepest, stopped around Dec 2024). That older range was still mostly unconverted, which is why this batch's raw-to-written yield (66/132 ≈ 50%) was much healthier than batch 6's (11/48 ≈ 23%).

## Collection funnel

| Stage | Count |
|---|---|
| Raw story URLs collected (one scroll session, `a[href*="/redirect"]` extraction) | 132 |
| Dropped — exact-URL duplicate of an existing recipe | 22 |
| Dropped — confirmed roundup/listicle (title-keyword match against known patterns) | 28 |
| Kept after first-pass filtering | 82 |
| Excluded pre-dispatch as likely roundup/informational on inspection | 4 |
| Dispatched to 6 parallel sub-agents (13 URLs each) | 78 |
| Written as new recipe files | **66** |
| Skipped by sub-agents after fetching (see below) | 12 |

## Written (66)

appetizers/burrata-with-tomatoes-and-pesto, beef/garlic-butter-bacon-cheeseburger, beef/one-pot-creamy-mushroom-ground-beef-stroganoff, beef/salisbury-steak, beverages/boba-tea, breads/focaccia, breads/homemade-naan, breads/mediterranean-spinach-feta-loaf, breakfast/high-protein-mediterranean-egg-casserole, desserts/bisquick-apple-cobbler, desserts/homemade-pistachio-cannoli, desserts/julie-andrews-carrot-cake, desserts/lemon-ricotta-cake, desserts/limoncello-bundt-cake, desserts/limoncello-tiramisu, desserts/no-bake-lemon-cheesecake, desserts/sourdough-carrot-cake-muffins, dips-spreads/blue-cheese-dressing, meat-mains/sausage-stuffed-butternut-squash, pasta/artichoke-pesto-pasta, pasta/canned-tuna-pasta, pasta/cherry-tomato-feta-pasta, pasta/creamy-feta-tomato-pasta, pasta/creamy-lemon-ricotta-pasta, pasta/creamy-ricotta-pesto-pasta, pasta/fabulous-fettuccine-with-creamy-mushroom-sauce, poultry/frango-com-quiabo-e-polenta, poultry/grilled-ginger-chicken-with-charred-peaches, poultry/juicy-greek-chicken, poultry/lemon-pepper-baked-chicken-drumsticks, poultry/savory-slow-cooker-mediterranean-balsamic-chicken, poultry/wine-chicken, salads/asparagus-and-pea-salad, salads/festive-watermelon-salad-with-feta, salads/greek-salmon-salad, salads/greek-tuna-stuffed-avocados, salads/ina-gartens-creamy-potato-salad, salads/italian-tuna-potato-salad, salads/lilos-authentic-german-potato-salad, salads/mediterranean-white-bean-salad-with-feta, salads/nicoise-salad (UNVERIFIED), salads/seafood-pasta-salad, salads/simple-is-best-arugula-salad, salads/tortellini-pasta-salad, salads/tuna-nicoise-salad, sandwiches/chickpea-salad-sandwich, sandwiches/italian-panini-sandwich (UNVERIFIED), sauces-dressings/lebanese-salad-dressing, sauces-dressings/sugar-free-honey-lime-dressing, seafood-mains/blackened-halibut-with-mango-avocado-relish, seafood-mains/cedar-plank-salmon (UNVERIFIED), seafood-mains/garlic-knot-salmon, seafood-mains/honey-garlic-glazed-salmon, sides/arroz-com-lula, sides/crispy-parmesan-potatoes, sides/crustless-spinach-feta-casserole, sides/easy-caribbean-rice-and-beans, sides/golden-red-lentil-dal-with-spinach, sides/lemon-basil-rice, sides/marry-me-chickpeas, sides/mediterranean-spinach-squares, sides/smashed-potatoes, sides/umami-fried-rice, soups/caldo-de-abobora-com-frango (UNVERIFIED), soups/smoked-salmon-and-leek-soup, soups/traditional-colombian-sancocho (UNVERIFIED).

4 files carry the `UNVERIFIED` tag (noted above) plus `julie-andrews-carrot-cake` and `limoncello-bundt-cake`, all for missing timing/servings the source never stated — never a guessed value.

## Skipped after fetching (12)

**Duplicates (7)** — same dish already in the cookbook, usually a same-article republish under a new date path/tip ID that the pre-dispatch exact-URL check didn't catch:
- Red Beans & Rice (30seconds.com tip 16654) — dup of `recipes/sides/red-beans-rice.md` (same tip ID)
- Patatas Bravas (gamintraveler.com, 2025/01/25) — dup of `recipes/appetizers/patatas-bravas.md` (republished article)
- $1000 Baked Spaghetti Pasta Casserole (30seconds.com tip 50933) — dup of `recipes/pasta/1000-baked-spaghetti-pasta-casserole.md`
- Amish Cabbage Soup (30seconds.com tip 31019) — dup of `recipes/soups/amish-cabbage-soup-with-ground-beef.md`
- Rib Roast (30seconds.com tip 13361) — dup of `recipes/beef/rib-roast-with-red-wine-jus.md`
- Baked Chicken Lombardy (30seconds.com tip 22172) — dup of `recipes/poultry/baked-chicken-lombardy.md`
- Gambas al Ajillo (gamintraveler.com, 2024/05/02) — dup of `recipes/seafood-mains/gambas-al-ajillo.md` (republished article)

**No real recipe content (4)**:
- "This 'So Buttery' Steakhouse-Cut Steak" (thekitchn.com) — resolves to a QVC product/affiliate-deal page for Rastelli's steaks, not a recipe
- "My German Husband Loves These Recipes: Just Like Oma" (inmamamaggieskitchen.com) — a 21-item roundup linking to other blogs, no standalone recipe on the page
- "Portuguese Feijoada Vs Brazilian Feijoada" (gamintraveler.com) — informational comparison article, no stated quantities or numbered steps
- Ina Garten's "Outrageous" Garlic Bread (simplyrecipes.com) — narrative review with no ingredient quantities (e.g. "an entire head" of garlic, "lots of" butter)

**Review page linking out (1)**:
- The 4-Ingredient, 10-Minute Dinner (cubbyathome.com) — review of a recipe hosted on TheKitchn.com; only a short excerpt is on the page itself, no full ingredients/steps

## Photo notes

Two recipes had their source `og:image` rejected per §7b's mismatch check and deliberately left without a photo (documented in each file's `## Missing Information`):
- `sides/mediterranean-spinach-squares.md` — og:image resolved to a completely different site's sourdough-carrot-cake-muffins photo
- `desserts/julie-andrews-carrot-cake.md` — the article's only image is a Getty portrait of Julie Andrews, not the cake

All other written recipes use `image_source_url` (none downloaded as `image_local` — this sandbox's outbound network allowlist blocks direct binary downloads to every source domain touched this batch, consistent with prior batches; the browser/fetch tools used to verify page content are unaffected).

## Sub-agent dispatch notes

Split 78 URLs across 6 parallel general-purpose sub-agents (~13 URLs each), each given the full schema (§5), naming convention (§4), anti-fabrication rule, mandatory photo verification (§7/§7b), and duplicate-detection instructions (§6c), per §6d. Agents were told to route gamintraveler.com, 30seconds.com, simplyrecipes.com, eatingwell.com, and receitas.globo.com URLs through the Claude-in-Chrome browser tools rather than raw fetch, per the standing finding from batches 4-5 that raw fetch is blocked or bot-walled on those domains.

## Next batch

Given this batch's yield (66) came from scrolling into a genuinely older, previously-unreached range (back to ~April 2024), batch 8 should keep pushing further back rather than expecting the same depth to still be fresh — a fresh scroll session restarts from the top per Flipboard's known behavior, so budget for at least as much scrolling as this batch (250+ actions) before extraction, and expect the yield curve to depend on how far past ~April 2024 the next session can reach.
