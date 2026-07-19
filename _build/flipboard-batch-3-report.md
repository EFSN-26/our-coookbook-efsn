---
name: flipboard-batch-3-report
last_updated: 2026-07-17
---

# Flipboard import — batch 3 report

Source: ["Food & Flavors" Flipboard magazine](https://flipboard.com/@enetoe/food-flavors-acbn0akgy) (@enetoe). This batch had two parts: (1) the 25 URLs banked at the end of batch 2 (collected during batch 2's scroll but not processed then, for capacity reasons), and (2) a fresh scroll of 139 story cards collected in this session (overlapping heavily with batches 1–2's already-seen range, since the scroll restarted from the top of the newest-first feed), from which 50 new single-recipe candidates were identified after duplicate/roundup filtering.

**Result: 56 new recipe files written (cookbook grew from 128 → 184 recipes).** 0 YAML errors, 0 duplicate `source_url` values across the full 184-file set after the build. 19 candidates were skipped (roundup/listicle, non-recipe, duplicate, or unreachable) — see below.

## Part 1 — banked candidates from batch 2 (25 processed, 14 written, 11 skipped)

**Written (14):**
- Easy Cassoulet (`recipes/poultry/easy-cassoulet.md`) — thekitchn.com
- Costolette di Maiale ai Funghi / Pork Chops with Mushroom Cream Sauce (`recipes/meat-mains/pork-chops-with-mushroom-cream-sauce.md`) — memoriediangelina.com
- Crispy Garlic Parmesan Tater Tots (`recipes/appetizers/crispy-garlic-parmesan-tater-tots.md`) — 30seconds.com
- Spooky Sweet Potato Ghost Hand Pies (`recipes/desserts/spooky-sweet-potato-ghost-hand-pies.md`) — tastingtable.com
- Tuscan White Bean Soup (`recipes/soups/tuscan-white-bean-soup.md`) — giangiskitchen.com
- Juicy Beef Steak Tips with Rich Mushroom Gravy (`recipes/beef/juicy-beef-steak-tips-with-mushroom-gravy.md`) — 30seconds.com
- Creamy Pumpkin Cheesecake Mousse (`recipes/desserts/creamy-pumpkin-cheesecake-mousse.md`) — 30seconds.com
- Fogo de Chao Picanha (Copycat) (`recipes/beef/fogo-de-chao-picanha.md`) — copykat.com
- No-Fuss Refrigerator Bread & Butter Pickles (`recipes/sides/refrigerator-bread-and-butter-pickles.md`) — 30seconds.com
- Honey Nut Granola (`recipes/breakfast/honey-nut-granola.md`) — thehonoursystem.com
- Garlic Parmesan Green Beans (`recipes/sides/garlic-parmesan-green-beans.md`) — gritsandpinecones.com
- Cheesy Hawaiian Garlic Rolls (`recipes/breads/cheesy-hawaiian-garlic-rolls.md`) — frontporchlifemagazine.com
- Ina Garten's Blueberry Ricotta Cake (`recipes/desserts/blueberry-ricotta-cake.md`) — 30seconds.com
- Baked Parmesan Zucchini Sticks (`recipes/sides/baked-parmesan-zucchini-sticks.md`) — masalaherb.com

**Skipped (11):**
- foodventuresabroad.com "Turn Any Night into an Italian Escape..." — roundup (10 linked pasta recipes)
- immigrantstable.com "17 Festive Vegan Recipes" — roundup (page tagged `category: Roundups`)
- simplyrecipes.com "Wine Chicken Recipe" — blocked domain (HTTP 403, confirmed still blocked)
- tastesdelicious.com "13 Soups That Will Keep Your Blood Sugar in Check" — roundup
- thehonoursystem.com "Classic Beef Stews" — roundup (10 linked recipes)
- xoxobella.com "14 Nonna-Approved Italian Soup Recipes" — unreachable (empty fetch) + roundup title pattern
- xoxobella.com "Bake Your Way to Heaven With 27 Bread Recipes" — unreachable + roundup title pattern
- southernliving.com "Pan-Seared Rib-Eye With Mushroom-Hunter's Sauce" — blocked (HTTP 403, domain-level block)
- xoxobella.com "Peanut Butter Spider Cookies" — unreachable (empty fetch)
- gamintraveler.com "How to Make Bacalhau à Brás" (2024/08/23 date-path) — unreachable (empty fetch; superseded later in this batch by a working 2foodtrippers.com source for the same dish)
- chowhound.com "The Brazilian Cocktail/Lemonade That's Ready to Conquer the World" — non-recipe article (food history/facts piece, no ingredient quantities or numbered steps)

## Part 2 — fresh scroll candidates (139 collected, 50 dispatched after filtering, 42 written, 8 skipped)

Collected via Claude in Chrome: navigated to the magazine, scrolled ~40 times (mouse-wheel, in bursts with waits for lazy-loading), and extracted each card's real outbound URL by decoding the `flipboard.com/redirect?url=...` wrapper directly from the DOM (`a[href*="/redirect"]`) rather than reading the accessibility tree card-by-card. 139 unique stories were collected total; most overlapped with batches 1–2's already-covered range (confirmed via exact `source_url` match), or were confirmed roundups/listicles by title pattern and spot-fetch, or were blocked domains (eatingwell.com, simplyrecipes.com, receitas.globo.com — 7 more receitas.globo.com bacalhau URLs seen again this session, still unconfirmed reachable). After filtering, 50 genuinely new, non-duplicate, non-roundup candidates were split into 4 chunks of 12–13 and dispatched to parallel sub-agents.

**Written (42):**

Group A (8 of 13): One-Pan Ground Beef and Vegetables (masalaherb.com), Greek Roasted Potatoes With Lemon & Feta (30seconds.com — confirmed genuinely distinct from the existing tip/42724 Greek-potatoes recipe: different technique, dressing, and added feta), Asparagus Salad (nutritiousdeliciousness.com), Creamy Applesauce Oatmeal (30seconds.com), Spinach Artichoke Stuffed Shells (nutritiousdeliciousness.com), Ground Beef Casserole (thehonoursystem.com), Tzatziki Recipe (xoxobella.com — confirmed distinct ratios from the existing gamintraveler.com tzatziki, filed as `tzatziki-xoxobella.md`; tagged UNVERIFIED, no photo retrievable), Amazing Pecan Pie Cake (30seconds.com).

Group B (10 of 13): Baked Brie with Honey, Walnuts, Figs, and Rosemary (gardenandgun.com), Coq au Vin (thekitchn.com), Easy 1-Pan Garlic Shrimp and Ramen Noodles (mashed.com), Pasta al Limón / Lemon Carbonara (30seconds.com — confirmed distinct from the existing cream-based Tagliatelle al Limone: this one is egg-yolk/guanciale carbonara-style), Pumpkin Pie Dessert Bars (casualepicure.com), Succulent Italian Pot Roast/Stracotto (30seconds.com), Best Roasted Vegetables (30seconds.com), Napa Valley Avocado & Corn Salad (30seconds.com), Creamy Mediterranean White Bean Salad (30seconds.com), Creamy Lemon Pasta (xoxobella.com — kept as a second, distinctly-sourced lemon pasta alongside the existing tagliatelle and the new pasta-al-limón, consistent with how this cookbook already keeps multiple variants of similar dishes; no photo retrievable).

Group C (12 of 12 — no skips): Greek Pasta Salad (cheerfulcook.com), Vanilla Chai Protein Smoothie (tastingtable.com), Watermelon Feta Salad with Honey Lime Dressing (sulaandspice.com), Mediterranean Lemony Lentil Salad (30seconds.com), Baked Halibut (beyondthechickencoop.com), Roasted Eggplant and Chickpea Buddha Bowl (lentillovingfamily.com — original URL now redirects to wholesomefamilymeals.com, noted in file), Lemony Shrimp Feta Pasta (30seconds.com), Mushroom Risotto (nutritiousdeliciousness.com), Apple Crunch Cheesecake (howtomakericecrispytreats.com), Spinach with Fettuccine (dizzybusyandhungry.com), Beet Salad with Feta and Mandarin Oranges (kellystilwell.com — confirmed distinct from the existing beet-and-feta-salad-with-pistachios-and-pears), Pan-Seared Lemon Caper Mahi Mahi (tastingtable.com).

Group D (12 of 12 — no skips): Creamy Garlic Parmesan Orzo (30seconds.com), Mediterranean Cream Cheese Dip (thegraciouspantry.com), Lamb Loin Chops (soufflebombay.com), Lemon Chicken & Rice Soup (30seconds.com), Bacalhau à Brás (2foodtrippers.com — confirmed a genuinely different dish from the existing Spanish Bacalao a la Vizcaína; extra photo scrutiny applied per the project's gamintraveler-mismatch precedent, no verifiable image URL found so left unset, tagged UNVERIFIED), Creamy Amish Cucumber Salad (30seconds.com), Colombian Chicken Sancocho (immigrantstable.com), Salmon Piccata with Spinach (ketocookingchristian.com), Linguine with Clams, Cherry Tomatoes, and Capers (americastestkitchen.com, UNVERIFIED — missing separate prep/cook split and difficulty), Hearty Lentil Soup with Chorizo and Spinach (americastestkitchen.com, UNVERIFIED — missing separate prep/cook split, cuisine, difficulty), Baked Mushroom Rice (twocityvegans.com), Bavarian Potato Salad (masalaherb.com).

**Skipped (8):**
- apartmenttherapy.com "The 130-Year-Old Italian Spaghetti Sauce Recipe..." — non-recipe (review article linking out twice to thekitchn.com for the actual recipe)
- gamintraveler.com "How to Make Fettuccine Alfredo" (2024/12/14) — unreachable (empty fetch)
- gamintraveler.com "How to Make Tuscan Chicken" (2024/12/30) — unreachable (empty fetch)
- gamintraveler.com "How to Make Aglio e Olio" (2024/12/24) — unreachable (empty fetch)
- gamintraveler.com "How to Make Chicken Tikka Masala" (2024/12/22) — unreachable (empty fetch); all four gamintraveler URLs in this specific sub-batch failed consistently, unlike gamintraveler recipes already in the cookbook — looks like a path-specific block rather than a domain-wide one
- bonappetit.com "Green Curry Coconut Cod" — blocked (HTTP 403, sandbox blocklist)
- cubbyathome.com "This $20 One-Pan Chicken Dinner..." — non-recipe (narrative review linking out to latimes.com for the actual recipe)
- thekitchn.com "I Made Kate Middleton's Beloved Watermelon Salad..." — non-recipe (narrative review linking out to womenshealthmag.com for the actual recipe)

## Confirmed roundups/listicles seen again or newly confirmed this batch (do not reconvert)
38 Winter Soups (thehonoursystem.com), Top 10 Salmon Recipes (simplyrecipes.com, also blocked), Most Delicious Stews (gamintraveler.com), 30 Seafood Recipes (littlebitrecipes.com), 25 One-Pot Anti-Inflammatory Dinners (eatingwell.com, also blocked), 32 Keto Seafood Dinners (ketocookingchristian.com), 17 One-Pan Meals (immigrantstable.com), 35 Italian Seafood Recipes/Feast of Seven Fishes (thekitchn.com), 31 Chicken Recipes (parallelplates.com), 15 Quick Christmas Treats (runningtothekitchen.com), 14 Classic Soup & Stew Recipes (littlebitrecipes.com — same one confirmed in batch 2), 15 Fall Soup Recipes (eatingwell.com, also blocked), 29 Shockingly Delicious Dinners (immigrantstable.com), 103 Old-Fashioned Church Cookbook Recipes (xoxobella.com), 14 Italian Recipes (littlebitrecipes.com), 27 Bread Recipes (xoxobella.com), 12 Baked Chicken Recipes (tastingtable.com), 17 Creamy Deli Salads (eatingwell.com, also blocked), 18 High-Protein Lentil Dinners (eatingwell.com, also blocked), 73 Ground Beef Recipes (xoxobella.com), 36 Pasta Salad Recipes (xoxobella.com), 30 Mocktail Recipes (mymocktailforest.com), 19 Summer Pasta Recipes (runningtothekitchen.com), 21 Picnic Salads (runningtothekitchen.com), 17 Noodle Recipes (allwaysdelicious.com), 19 Sides and Salads (littlebitrecipes.com), 15 Vintage Recipes (tastesdelicious.com), Grandma's 11 Homestyle Recipes (immigrantstable.com), 28 Lemonade Recipes (xoxobella.com), 14 Pork Recipes (afoodloverskitchen.com — confirmed again from batch 2), 18 Delicious Dinners (thrivinginparenting.com).

## Blocked/unreachable domains this batch
- **eatingwell.com, simplyrecipes.com, receitas.globo.com** — still blocked, consistent with batches 1–2. 7 more receitas.globo.com bacalhau/salt-cod URLs surfaced in this session's scroll; still unverifiable.
- **xoxobella.com** — mixed results: 2 of 4 URLs attempted this batch succeeded (tzatziki, creamy-lemon-pasta), 2 returned empty fetches. Reachability appears intermittent/path-dependent rather than a hard domain block.
- **southernliving.com** — one URL returned HTTP 403 this batch (differs from batch 2, where a different southernliving.com URL was fetched successfully) — appears to be a per-URL or per-path block, not domain-wide.
- **gamintraveler.com** — 5 of 5 URLs attempted in the fresh-scroll candidates this batch (all older, 2024-dated articles) returned empty fetches, while gamintraveler.com URLs already in the cookbook (mostly 2025–2026-dated) work fine. Possibly an archival/older-URL-specific issue on their end.
- **bonappetit.com** — one URL blocked (HTTP 403, sandbox blocklist).

## Photos
Sub-agents applied the mandatory og:image sanity check (`_cookbook-meta-prompt.md` §7b) per recipe, with extra scrutiny requested (and applied) for the Bacalhau à Brás candidate given this project's prior gamintraveler bacalhau/salmorejo image-mismatch incident. Direct image downloads via `curl`/`wget` failed for essentially every recipe this batch — the sandbox's outbound proxy blocked all arbitrary hosts (`403`/`blocked-by-allowlist`/connection failures) — so all 56 new recipes use `image_source_url` (a verified og:image URL) rather than a locally downloaded `image_local`, except 3 recipes where no image URL could be extracted at all (xoxobella tzatziki, xoxobella creamy-lemon-pasta, 2foodtrippers bacalhau à brás) — these fall back to the same-category photo-borrowing rule or a plain initials tile and are noted in `## Missing Information`.

## Build verification
`python3 _build/build.py` completed cleanly on the first run (no OneDrive/bash staleness issue this time): 184 recipes across 17 categories, 0 parse errors, 0 duplicate source URLs. `index.html` ends correctly (`</script>\n</body>\n</html>`, 968 KB), confirming no truncation. 6 recipes still show the same-category fallback photo (listed in the build's own report): tzatziki-xoxobella, creamy-lemon-pasta, sheet-pan-garlic-butter-gnocchi-with-summer-vegetables (carried over from batch 2), bacalao-a-la-vizcaina (carried over), bacalhau-a-bras (new), chicken-and-sausage-gumbo-with-dark-roux (carried over).
