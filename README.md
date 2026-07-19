# Our Cookbook

A Markdown-based personal recipe library with a standalone, searchable HTML browser. See `_cookbook-meta-prompt.md` for the full spec.

## Browse it

Double-click **`index.html`** to open the cookbook site in your browser — no install, no server. Search, filter by category, star a recipe as a favorite and browse just your favorites, open a recipe, and scale servings live.

Every recipe page leads with its description and a compact Prep / Cook / Total / Difficulty box in the top-left corner (any of the four that's missing shows "N.A." rather than being left blank), a clickable source link right below the description, and every card/banner always shows a photo — recipes without their own yet borrow one from another recipe **in the same category only** (never an unrelated dish), clearly labeled as such, or fall back to a plain initials tile if no same-category photo exists either. Clicking a category in the sidebar always shows that category's recipes, even if you'd typed something into the search box first — and the reverse holds too: typing a search keyword always searches every recipe, switching back to "All Recipes" even if a category or ★ Favorites filter was active.

`index.html` is generated from the Markdown files in `recipes/`. It rebuilds automatically whenever you ask Claude to add or edit a recipe. To rebuild it yourself: `python3 _build/build.py`.

## Current recipes

226 recipes across 17 categories. Recipes flagged ⚠️ incomplete/unverified are missing a detail the source didn't state (usually an exact time, servings count, or difficulty) — never a guessed value; open the file's "Missing Information" section to see exactly what's missing, or check the site for the same warning banner (shown at the bottom of the recipe page, below the Print Recipe button).

**Appetizers**
- [Baked Brie with Honey, Walnuts, Figs, and Rosemary](recipes/appetizers/baked-brie-with-the-works.md) — 25 min, 4 servings
- [Crispy Garlic Parmesan Tater Tots](recipes/appetizers/crispy-garlic-parmesan-tater-tots.md) — 30 min, 8 servings — ⚠️ incomplete/unverified
- [Crispy Potato Cheese Croquettes](recipes/appetizers/potato-cheese-croquettes.md) — 50 min — ⚠️ incomplete/unverified
- [Ina Garten's Cauliflower Toast](recipes/appetizers/ina-gartens-cauliflower-toast.md) — details pending — ⚠️ incomplete/unverified
- [Patatas Bravas](recipes/appetizers/patatas-bravas.md) — details pending — ⚠️ incomplete/unverified

**Beef**
- [Boeuf Bourguignon](recipes/beef/boeuf-bourguignon.md) — 360 min, 6 servings — ⚠️ incomplete/unverified
- [Fall-Off-the-Bone Braised Short Ribs](recipes/beef/braised-short-ribs-in-red-wine.md) — 195 min, 6 servings
- [Fogo de Chao Picanha (Copycat)](recipes/beef/fogo-de-chao-picanha.md) — 35 min, 8 servings
- [Ground Beef Casserole](recipes/beef/ground-beef-and-potato-casserole.md) — 95 min, 6 servings
- [Juicy Beef Steak Tips with Rich Mushroom Gravy](recipes/beef/juicy-beef-steak-tips-with-mushroom-gravy.md) — 45 min, 4 servings
- [Maminha com Manteiga Temperada](recipes/beef/maminha-com-manteiga-temperada.md) — 60 min, 5 servings — ⚠️ incomplete/unverified
- [One-Pan Ground Beef and Vegetables](recipes/beef/one-pan-ground-beef-and-mixed-vegetables.md) — 45 min, 3 servings
- [Rib Roast With Red Wine Jus](recipes/beef/rib-roast-with-red-wine-jus.md) — 12 servings — ⚠️ incomplete/unverified
- [Shortcut Budget Beef Tips With Savory Brown Gravy](recipes/beef/budget-beef-tips-with-brown-gravy.md) — 130 min, 8 servings — ⚠️ incomplete/unverified
- [Spanish Oxtail Stew (Rabo de Toro)](recipes/beef/spanish-oxtail-stew.md) — 270 min, 6 servings
- [Succulent Italian Pot Roast (Stracotto)](recipes/beef/italian-pot-roast-stracotto.md) — 210 min, 8 servings

**Beverages**
- [Easy Homemade Watermelon Lemonade](recipes/beverages/watermelon-lemonade.md) — 10 min — ⚠️ incomplete/unverified
- [Fresh Lemon Cucumber Mint Water](recipes/beverages/lemon-cucumber-mint-water.md) — 5 min — ⚠️ incomplete/unverified
- [Lemon Cucumber Mint Infused Water](recipes/beverages/lemon-cucumber-mint-infused-water.md) — 490 min, 6 servings — ⚠️ incomplete/unverified
- [Vanilla Chai Protein Smoothie](recipes/beverages/vanilla-chai-protein-smoothie.md) — 5 min, 2 servings
- [Whipped Strawberry Lemonade](recipes/beverages/whipped-strawberry-lemonade.md) — 70 min, 4 servings

**Breads**
- [Amish Cornbread](recipes/breads/amish-cornbread.md) — 27 min, 9 servings
- [Cheese Bread (Pão de Queijo style)](recipes/breads/cheese-bread.md) — details pending — ⚠️ incomplete/unverified
- [Cheesy Hawaiian Garlic Rolls](recipes/breads/cheesy-hawaiian-garlic-rolls.md) — 15 min, 9 servings
- [Nonna's No-Knead Pizza Dough](recipes/breads/no-knead-pizza-dough.md) — 30 min, 16 servings
- [One Dough, Four Breads Europeans Actually Eat On Weeknights](recipes/breads/one-dough-four-breads.md) — 120 min, 10 servings
- [Whole-Loaf Cheesy Garlic Bread](recipes/breads/whole-loaf-cheesy-garlic-bread.md) — 4-8 servings — ⚠️ incomplete/unverified

**Breakfast**
- [Apricot-Pistachio Overnight Oats](recipes/breakfast/apricot-pistachio-overnight-oats.md) — 495 min, 4 servings — ⚠️ incomplete/unverified
- [Avocado Toast Three Ways](recipes/breakfast/avocado-toast-three-ways.md) — 20 min, 8 servings
- [Cheesy Baked Polenta and Egg with Bacon](recipes/breakfast/cheesy-baked-polenta-and-egg-with-bacon.md) — 40 min, 2 servings
- [Creamy Applesauce Oatmeal](recipes/breakfast/creamy-applesauce-oatmeal.md) — 5 min, 1 servings
- [Honey Nut Granola](recipes/breakfast/honey-nut-granola.md) — 50 min, 8 servings

**Desserts**
- [Amazing Pecan Pie Cake](recipes/desserts/pecan-pie-cake.md) — 70 min, 12 servings
- [Apple Crunch Cheesecake](recipes/desserts/apple-crunch-cheesecake.md) — 90 min, 8 servings
- [Buttery Bread Pudding With Bourbon Butter Sauce](recipes/desserts/buttery-bread-pudding-with-bourbon-butter-sauce.md) — 75 min, 12 servings
- [Creamy Key Lime Pie with Buttery Graham Cracker Crust](recipes/desserts/key-lime-pie.md) — 45 min, 8 servings
- [Creamy Pineapple Sherbet](recipes/desserts/creamy-pineapple-sherbet.md) — 160 min, 4 servings — ⚠️ incomplete/unverified
- [Creamy Pumpkin Cheesecake Mousse](recipes/desserts/creamy-pumpkin-cheesecake-mousse.md) — 10 min, 6 servings
- [Date and Walnut Cake](recipes/desserts/date-and-walnut-cake.md) — 60 min, 8 servings
- [Ina Garten's Blueberry Ricotta Cake](recipes/desserts/blueberry-ricotta-cake.md) — 70 min, 8 servings
- [Italian Lemon Cream Cake](recipes/desserts/italian-lemon-cream-cake.md) — 60 min, 8 servings — ⚠️ incomplete/unverified
- [No-Bake Boston Cream Pie Bars](recipes/desserts/no-bake-boston-cream-pie-bars.md) — details pending — ⚠️ incomplete/unverified
- [Peanut Butter Fandango Rice Krispies Treats](recipes/desserts/peanut-butter-fandango-rice-krispies-treats.md) — 30 min, 12 servings
- [Pumpkin Pie Dessert Bars](recipes/desserts/pumpkin-pie-dessert-bars.md) — 70 min, 16 servings
- [Rabanada da Solange Couto](recipes/desserts/rabanada-da-solange-couto.md) — 30 min, 10 servings
- [Spooky Sweet Potato Ghost Hand Pies](recipes/desserts/spooky-sweet-potato-ghost-hand-pies.md) — 80 min, 16 servings
- [Swedish Apple Cake](recipes/desserts/swedish-apple-cake.md) — 60 min, 8 servings — ⚠️ incomplete/unverified
- [Tiramisu](recipes/desserts/tiramisu.md) — details pending — ⚠️ incomplete/unverified

**Dips & Spreads**
- [Authentic Restaurant-Style Italian Bread Dipping Oil](recipes/dips-spreads/italian-bread-dipping-oil.md) — 5 min, 20 servings
- [Avocado Hummus](recipes/dips-spreads/avocado-hummus.md) — 15 min, 6 servings
- [Beet Hummus](recipes/dips-spreads/beet-hummus.md) — 50 min, 6 servings
- [Chocolate Brownie Batter Hummus](recipes/dips-spreads/chocolate-brownie-batter-hummus.md) — 65 min, 12 servings
- [Creamy Black-Eyed Pea Hummus](recipes/dips-spreads/black-eyed-pea-hummus.md) — 7 min, 6 servings
- [Mediterranean Cream Cheese Dip](recipes/dips-spreads/mediterranean-cream-cheese-dip.md) — 15 min, 4 servings
- [Mediterranean Lemon Basil Vinaigrette](recipes/dips-spreads/lemon-basil-vinaigrette.md) — 10 min, 8 servings — ⚠️ incomplete/unverified
- [Mexican-Style Black Bean Hummus](recipes/dips-spreads/mexican-style-black-bean-hummus.md) — 15 min, 6 servings
- [Pineapple Serrano Hummus](recipes/dips-spreads/pineapple-serrano-hummus.md) — details pending — ⚠️ incomplete/unverified
- [Roasted Carrot Hummus](recipes/dips-spreads/roasted-carrot-hummus.md) — 33 min, 6 servings
- [Roasted Red Pepper Hummus](recipes/dips-spreads/roasted-red-pepper-hummus.md) — 25 min, 6 servings
- [Smooth Garlic Hummus (Israeli-Style)](recipes/dips-spreads/smooth-garlic-hummus.md) — 165 min, 4 servings
- [Spicy Harissa Hummus](recipes/dips-spreads/harissa-hummus.md) — 5 min, 6 servings
- [Sweet Potato Hummus](recipes/dips-spreads/sweet-potato-hummus.md) — 30 min, 4 servings
- [Tzatziki](recipes/dips-spreads/tzatziki.md) — details pending — ⚠️ incomplete/unverified
- [Tzatziki Recipe](recipes/dips-spreads/tzatziki-xoxobella.md) — 75 min, 4 servings — ⚠️ incomplete/unverified
- [White Bean Hummus with Feta](recipes/dips-spreads/white-bean-hummus-feta.md) — 10 min, 6 servings
- [Zucchini Hummus](recipes/dips-spreads/zucchini-hummus.md) — 5 min, 8 servings

**Meat Mains**
- [Costolette di Maiale ai Funghi (Pork Chops with Mushroom Cream Sauce)](recipes/meat-mains/pork-chops-with-mushroom-cream-sauce.md) — 60 min, 4 servings — ⚠️ incomplete/unverified
- [Cotoletta alla Milanese](recipes/meat-mains/cotoletta-alla-milanese.md) — 4 servings — ⚠️ incomplete/unverified
- [Herb Crusted Pork Tenderloin With Mushroom Gravy](recipes/meat-mains/herb-crusted-pork-tenderloin-with-mushroom-gravy.md) — 30 min, 6 servings
- [Lamb Loin Chops](recipes/meat-mains/lamb-loin-chops.md) — 25 min, 3 servings
- [Slow Cooker Lamb Shanks With Red Wine Gravy](recipes/meat-mains/slow-cooker-lamb-shanks-with-red-wine-gravy.md) — 530 min, 2 servings
- [The Best Meatballs Ever! (Italian Polpette Recipe)](recipes/meat-mains/polpette-italian-meatballs-in-tomato-sauce.md) — 55 min, 4-6 servings

**Pasta**
- [$1000 Baked Spaghetti Pasta Casserole](recipes/pasta/1000-baked-spaghetti-pasta-casserole.md) — 50 min, 6 servings
- [Authentic Spaghetti Bolognese](recipes/pasta/authentic-spaghetti-bolognese.md) — 80 min, 4 servings
- [Authentic Spaghetti Carbonara](recipes/pasta/spaghetti-carbonara.md) — details pending — ⚠️ incomplete/unverified
- [BLT Carbonara](recipes/pasta/blt-carbonara.md) — 40 min, 4 servings
- [Cheesy Italian Penne Pasta with Sundried Tomatoes](recipes/pasta/cheesy-italian-penne-pasta-with-sundried-tomatoes.md) — 15 min, 4 servings
- [Creamy Boursin Orzo with Spinach](recipes/pasta/creamy-boursin-orzo-with-spinach.md) — 15 min, 6 servings
- [Creamy Boursin Pasta With Roasted Vegetables & Chicken](recipes/pasta/creamy-boursin-pasta-with-roasted-vegetables-chicken.md) — 50 min, 6 servings — ⚠️ incomplete/unverified
- [Creamy Cajun Sausage Spaghetti](recipes/pasta/creamy-cajun-sausage-spaghetti.md) — 40 min, 2 servings — ⚠️ incomplete/unverified
- [Creamy Corn Orzo](recipes/pasta/creamy-corn-orzo.md) — 4 servings — ⚠️ incomplete/unverified
- [Creamy Garlic Parmesan Orzo](recipes/pasta/creamy-garlic-parmesan-orzo.md) — 20 min, 6 servings
- [Creamy Greek Spinach Orzo with Feta](recipes/pasta/creamy-greek-spinach-orzo-with-feta.md) — 30 min, 4 servings
- [Creamy Ground Beef Alfredo Pasta](recipes/pasta/creamy-ground-beef-alfredo-pasta.md) — 20 min, 6 servings
- [Creamy Lemon Pasta (Pasta al Limone)](recipes/pasta/creamy-lemon-pasta.md) — 30 min, 4 servings
- [Creamy Spinach Artichoke Pasta Casserole](recipes/pasta/creamy-spinach-artichoke-pasta-casserole.md) — 35 min, 6 servings — ⚠️ incomplete/unverified
- [Lemony Shrimp Feta Pasta](recipes/pasta/lemony-shrimp-feta-pasta.md) — 20 min, 4 servings
- [Pasta al Limón (Lemon Carbonara)](recipes/pasta/pasta-al-limon.md) — 20 min, 6 servings
- [Pasta alla Norma](recipes/pasta/pasta-alla-norma.md) — details pending — ⚠️ incomplete/unverified
- [Prisoner's Pasta (Pasta alla Carcerata)](recipes/pasta/prisoners-pasta.md) — 27 min, 3 servings
- [Quick Italian Sausage Pasta with Tomato Cream Sauce](recipes/pasta/quick-italian-sausage-pasta-with-tomato-cream-sauce.md) — 20 min, 5 servings
- [Sausage-Broccoli Pasta](recipes/pasta/sausage-broccoli-pasta.md) — details pending — ⚠️ incomplete/unverified
- [Sheet-Pan Garlic-Butter Gnocchi With Summer Vegetables](recipes/pasta/sheet-pan-garlic-butter-gnocchi-with-summer-vegetables.md) — 40 min, 4 servings — ⚠️ incomplete/unverified
- [Sizzling Spaghetti](recipes/pasta/sizzling-spaghetti.md) — details pending — ⚠️ incomplete/unverified
- [Spaghetti Aglio e Olio](recipes/pasta/spaghetti-aglio-e-olio.md) — 15 min, 2 servings — ⚠️ incomplete/unverified
- [Spaghetti alla Puveriello (Poor Man's Spaghetti)](recipes/pasta/spaghetti-alla-puveriello-poor-mans-spaghetti.md) — 25 min, 2 servings
- [Spinach Artichoke Stuffed Shells](recipes/pasta/spinach-artichoke-stuffed-shells.md) — 45 min, 8 servings
- [Spinach with Fettuccine](recipes/pasta/fettuccine-and-spinach.md) — 20 min, 4 servings
- [Spinach-And-Sun-Dried Tomato Pasta](recipes/pasta/spinach-sun-dried-tomato-pasta-with-chicken.md) — 20 min, 6-8 servings
- [Tagliatelle al Limone (Lemon Sauce)](recipes/pasta/tagliatelle-al-limone.md) — details pending — ⚠️ incomplete/unverified
- [Tagliatelle al Ragù](recipes/pasta/tagliatelle-al-ragu.md) — 180-300 min, 4 servings — ⚠️ incomplete/unverified
- [Tagliatelle al Tartufo Truffle Sauce](recipes/pasta/tagliatelle-al-tartufo-truffle-sauce.md) — 30 min, 4 servings
- [The Godfather's Sunday Gravy](recipes/pasta/godfathers-sunday-gravy.md) — 10 servings — ⚠️ incomplete/unverified
- [This Creamy Lemon Rigatoni Is All I'm Making This Week for Dinner](recipes/pasta/creamy-lemon-cottage-cheese-rigatoni.md) — 30 min, 6 servings — ⚠️ incomplete/unverified
- [Tomato Cottage Cheese Pasta Sauce](recipes/pasta/tomato-cottage-cheese-pasta-sauce.md) — 20 min, 4 servings — ⚠️ incomplete/unverified

**Poultry**
- [Apple Cider Chicken Thighs](recipes/poultry/apple-cider-chicken-thighs.md) — 40 min, 4 servings
- [Bahrain Spiced Chicken & Rice (Chicken Machboos)](recipes/poultry/bahrain-chicken-machboos.md) — 75 min, 4 servings — ⚠️ incomplete/unverified
- [Baked Chicken Lombardy](recipes/poultry/baked-chicken-lombardy.md) — 35 min, 4 servings
- [Classic Creamy Tuscan Chicken](recipes/poultry/classic-creamy-tuscan-chicken.md) — 40 min, 4 servings
- [Coq au Vin](recipes/poultry/coq-au-vin.md) — 100 min, 6 servings
- [Easy Broccoli Cashew Chicken Stir Fry](recipes/poultry/broccoli-cashew-chicken-stir-fry.md) — 30 min, 6 servings
- [Easy Cassoulet](recipes/poultry/easy-cassoulet.md) — 75 min, 4 servings
- [Healthier Creamy Tuscan Chicken (Slow Cooker or Instant Pot)](recipes/poultry/healthier-creamy-tuscan-chicken-slow-cooker-instant-pot.md) — 6 servings
- [Homemade Chicken Tikka Masala](recipes/poultry/homemade-chicken-tikka-masala.md) — 90 min, 4 servings
- [Magic Mayo Parmesan Baked Chicken](recipes/poultry/magic-mayo-parmesan-baked-chicken.md) — 25 min, 4 servings
- [Mediterranean Sausage and White Bean Skillet](recipes/poultry/mediterranean-sausage-white-bean-skillet.md) — 25 min, 2 to 4 servings — ⚠️ incomplete/unverified
- [Nonna's Sundried Tomato Italian Chicken](recipes/poultry/nonnas-sundried-tomato-italian-chicken.md) — 190 min, 8 servings — ⚠️ incomplete/unverified
- [Shortcut French Chicken](recipes/poultry/french-chicken.md) — 6 servings — ⚠️ incomplete/unverified

**Salads**
- [Apple Cranberry Slaw](recipes/salads/apple-cranberry-slaw.md) — 20 min, 8 servings
- [Asparagus Salad](recipes/salads/asparagus-salad.md) — 15 min, 6 servings
- [Balsamic Spinach Strawberry Feta Salad with Walnuts](recipes/salads/balsamic-spinach-strawberry-feta-salad-with-walnuts.md) — 8 min, 3 servings
- [Bavarian Potato Salad](recipes/salads/bavarian-potato-salad.md) — 15 min, 4 servings
- [Beet Salad with Feta](recipes/salads/beet-salad-with-feta-and-mandarin-oranges.md) — 70 min, 4 servings
- [Beet and Feta Salad with Pistachios and Pears](recipes/salads/beet-and-feta-salad-with-pistachios-and-pears.md) — 15 min, 2 servings
- [Chickpea, Beet & Cucumber Salad](recipes/salads/chickpea-beet-cucumber-salad.md) — 20 min, 6 servings — ⚠️ incomplete/unverified
- [Crab Salad](recipes/salads/crab-salad.md) — 15 min, 6 servings
- [Creamy Amish Cucumber Salad](recipes/salads/creamy-amish-cucumber-salad.md) — 10 min, 6 servings
- [Creamy Green Bean Potato Salad With Avocado Dressing](recipes/salads/green-bean-potato-salad-with-avocado-dressing.md) — 50 min, 8 servings — ⚠️ incomplete/unverified
- [Creamy Mediterranean White Bean Salad](recipes/salads/mediterranean-white-bean-salad.md) — 20 min, 8 servings
- [Cucumber Dill Salad](recipes/salads/cucumber-dill-salad.md) — 10 min — ⚠️ incomplete/unverified
- [Cucumber Salad](recipes/salads/creamy-cucumber-salad.md) — 70 min, 4 servings
- [Cucumber Salad with Herbs and Pine Nuts](recipes/salads/cucumber-salad-with-herbs-and-pine-nuts.md) — 10 min, 6 servings
- [Dill Pickle Ranch Potato Salad](recipes/salads/dill-pickle-ranch-potato-salad.md) — 110 min, 12 servings — ⚠️ incomplete/unverified
- [French Bistro Salad with Punchy Dijon Vinaigrette](recipes/salads/french-bistro-salad-with-dijon-vinaigrette.md) — 10 min, 4 servings
- [French Lentil Salad](recipes/salads/french-lentil-salad.md) — 35 min, 6 servings
- [Goat Cheese Salad With Green Beans](recipes/salads/goat-cheese-salad-with-green-beans.md) — 4 servings
- [Greek Pasta Salad](recipes/salads/greek-pasta-salad.md) — 20 min, 8 servings
- [High-Fiber Chickpea & Farro Salad with Artichokes & Tomatoes](recipes/salads/chickpea-farro-salad-with-artichokes-and-tomatoes.md) — 20 min, 8 servings
- [High-Fiber Cucumber Avocado Salad](recipes/salads/cucumber-avocado-salad.md) — 10 min, 6 servings — ⚠️ incomplete/unverified
- [High-Protein Caprese Salad](recipes/salads/high-protein-caprese-salad.md) — 5 min, 2 servings — ⚠️ incomplete/unverified
- [High-Protein No-Mayonnaise Tuna Salad](recipes/salads/high-protein-no-mayonnaise-tuna-salad.md) — 10 min, 3 servings
- [Lemon-Garlic Dense Bean Salad with Feta](recipes/salads/lemon-garlic-dense-bean-salad-with-feta.md) — 20 min, 4 servings — ⚠️ incomplete/unverified
- [Mediterranean Chickpea Cucumber Salad](recipes/salads/mediterranean-chickpea-cucumber-salad.md) — 15 min, 6 servings
- [Mediterranean Lemony Lentil Salad](recipes/salads/mediterranean-lemony-lentil-salad.md) — 30 min, 8 servings
- [Mediterranean Potato Salad With Smashed Olives and Mint](recipes/salads/mediterranean-potato-salad-with-smashed-olives-and-mint.md) — 30 min, 10 servings
- [Mexican Street Corn-Inspired Bean Salad](recipes/salads/mexican-street-corn-inspired-bean-salad.md) — 10 min, 6 servings
- [Napa Valley Avocado & Corn Salad with Creamy Feta Dressing](recipes/salads/napa-valley-avocado-corn-salad.md) — 30 min, 6 servings
- [Peach Blueberry Cucumber Salad with Feta in Lemon Basil Vinaigrette](recipes/salads/peach-blueberry-cucumber-salad-with-feta.md) — 15 min, 6 servings
- [Radish Salad](recipes/salads/radish-salad.md) — 4 servings — ⚠️ incomplete/unverified
- [Red Potato Salad](recipes/salads/red-potato-salad.md) — 6 servings
- [Roasted Eggplant and Chickpea Buddha Bowl](recipes/salads/roasted-eggplant-and-chickpea-buddha-bowl.md) — 20 min, 2 servings
- [Roasted Potato Tzatziki Bowls](recipes/salads/roasted-potato-tzatziki-bowls.md) — 45 min, 4 servings
- [Salada de grão-de-bico com cebola marinada](recipes/salads/chickpea-salad-with-marinated-onion.md) — 30 min, 6 servings
- [Strawberry Spinach Salad with Fresh Oranges](recipes/salads/strawberry-spinach-salad-with-fresh-oranges.md) — 10 min, 4 servings
- [Thanksgiving Slaw](recipes/salads/thanksgiving-slaw.md) — 15 min, 8 servings — ⚠️ incomplete/unverified
- [Three Bean Salad](recipes/salads/three-bean-salad.md) — 25 min, 8 servings
- [Watermelon Feta Salad with Honey Lime Dressing](recipes/salads/watermelon-feta-salad-with-honey-lime-dressing.md) — 15 min, 4 servings

**Sandwiches**
- [Cheddar Tomato Sandwich, a Tomato Farmer's Method](recipes/sandwiches/cheddar-tomato-sandwich-farmers-method.md) — 1 servings — ⚠️ incomplete/unverified
- [Ham and Cheese Toast (4 Ingredients)](recipes/sandwiches/ham-and-cheese-toast.md) — 6 min, 2 servings — ⚠️ incomplete/unverified
- [Marv 'n' Joe Tomato Sandwich](recipes/sandwiches/marv-n-joe-tomato-sandwich.md) — 2 servings — ⚠️ incomplete/unverified
- [Tyler Smith's French Bread Pizza](recipes/sandwiches/french-bread-pizza.md) — 30 min, 4 servings

**Sauces**
- [Richard and Suzanne's Famous Spaghetti Sauce](recipes/sauces/richard-and-suzannes-spaghetti-sauce.md) — 25 min, 6 servings — ⚠️ incomplete/unverified

**Sauces & Dressings**
- [Garlic-Dijon Vinaigrette](recipes/sauces-dressings/garlic-dijon-vinaigrette.md) — 10 min, 16 servings
- [Lemon-Dill Vinaigrette](recipes/sauces-dressings/lemon-dill-vinaigrette.md) — 5 min, 6 servings — ⚠️ incomplete/unverified

**Seafood Mains**
- [Bacalao a la Vizcaína](recipes/seafood-mains/bacalao-a-la-vizcaina.md) — details pending — ⚠️ incomplete/unverified
- [Bacalhau ao forno com batatas e azeitonas pretas](recipes/seafood-mains/bacalhau-ao-forno-com-batatas-e-azeitonas-pretas.md) — 60 min, 6 servings
- [Bacalhau à Brás](recipes/seafood-mains/bacalhau-a-bras.md) — 2220 min, 4 as an appetizer, 2 as a main course servings — ⚠️ incomplete/unverified
- [Back-to-Basics: How to Make Salmon on the Griddle](recipes/seafood-mains/griddled-salmon.md) — details pending — ⚠️ incomplete/unverified
- [Baked Halibut](recipes/seafood-mains/baked-halibut.md) — 25 min, 4 servings
- [Buttery Garlic Lemon Shrimp](recipes/seafood-mains/buttery-garlic-lemon-shrimp.md) — 10 min, 4 servings
- [Cider-Glazed Salmon](recipes/seafood-mains/cider-glazed-salmon.md) — 30 min, 2 servings
- [Creamy Garlic Shrimp Recipe Is the Best Thing You'll Eat All Week (20 Minutes, 7 Ingredients)](recipes/seafood-mains/creamy-garlic-shrimp.md) — 20 min, 6 servings
- [Easy 1-Pan Garlic Shrimp and Ramen Noodles](recipes/seafood-mains/garlic-shrimp-ramen-noodles.md) — 30 min, 4 servings
- [Gambas al Ajillo (Spanish Garlic Shrimp)](recipes/seafood-mains/gambas-al-ajillo.md) — details pending — ⚠️ incomplete/unverified
- [Lemon-Garlic Salmon & Broccoli Bowls](recipes/seafood-mains/lemon-garlic-salmon-broccoli-bowls.md) — 30 min, 4 servings
- [Linguine with Clams, Cherry Tomatoes, and Capers](recipes/seafood-mains/linguine-with-clams-cherry-tomatoes-and-capers.md) — 45 min, 4 servings — ⚠️ incomplete/unverified
- [Marmitako (Basque Tuna and Potato Stew)](recipes/seafood-mains/marmitako-basque-tuna-potato-stew.md) — 60 min, 4 servings — ⚠️ incomplete/unverified
- [One-Pan Salmon with Creamy Caper Sauce](recipes/seafood-mains/one-pan-salmon-with-creamy-caper-sauce.md) — 15 min, 4 servings
- [Pan-Seared Lemon Caper Mahi Mahi](recipes/seafood-mains/pan-seared-lemon-caper-mahi-mahi.md) — 85 min, 4 servings
- [Panko-Crusted Baked Salmon](recipes/seafood-mains/panko-crusted-baked-salmon.md) — 20 min, 4 servings
- [Salada de bacalhau com batata e azeitona](recipes/seafood-mains/salada-de-bacalhau-com-batata-e-azeitona.md) — 30 min, 10 servings
- [Salmon Piccata with Spinach](recipes/seafood-mains/salmon-piccata-with-spinach.md) — 20 min, 6 servings
- [Sheet Pan Mediterranean Garlic Butter Baked Salmon](recipes/seafood-mains/sheet-pan-mediterranean-garlic-butter-baked-salmon.md) — 25 min, 6 servings
- [Shrimp Scampi](recipes/seafood-mains/shrimp-scampi.md) — details pending — ⚠️ incomplete/unverified

**Sides**
- [Baked Mushroom Rice](recipes/sides/baked-mushroom-rice.md) — 40 min, 4 servings
- [Baked Parmesan Zucchini Sticks](recipes/sides/baked-parmesan-zucchini-sticks.md) — 80 min, 40 servings
- [Best Roasted Vegetables](recipes/sides/best-roasted-vegetables.md) — 40 min, 8 servings
- [Buttery Garlicky Cannellini Beans With Feta and Sumac](recipes/sides/buttery-garlicky-cannellini-beans-with-feta-and-sumac.md) — 25 min, 4 servings
- [Cabbage & Potatoes with Bacon](recipes/sides/cabbage-and-potatoes-with-bacon.md) — 25 min, 6 servings
- [Craveable Cauliflower Alfredo Casserole With Peas & Bacon](recipes/sides/cauliflower-alfredo-casserole-with-peas-and-bacon.md) — 40 min, 6 servings
- [Creamy French Onion White Beans](recipes/sides/creamy-french-onion-white-beans.md) — 55 min, 6 servings — ⚠️ incomplete/unverified
- [Decadent Boursin Creamed Spinach With Mushrooms](recipes/sides/boursin-creamed-spinach-with-mushrooms.md) — 15 min, 6 servings
- [Easy Red Beans & Rice](recipes/sides/red-beans-rice.md) — 25 min, 6 servings — ⚠️ incomplete/unverified
- [Farofa de Natal](recipes/sides/farofa-de-natal.md) — 30 min, 10 servings
- [Garlic Herb Sauteed Mushrooms](recipes/sides/garlic-herb-sauteed-mushrooms.md) — 10 min, 4 servings
- [Garlic Parmesan Green Beans (Blistered)](recipes/sides/garlic-parmesan-green-beans.md) — 15 min, 4 servings
- [Grandma's Orange Ginger Carrots](recipes/sides/grandmas-orange-ginger-carrots.md) — 20 min, 8 servings — ⚠️ incomplete/unverified
- [Greek Roasted Potatoes Recipe With Lemon & Feta](recipes/sides/greek-roasted-potatoes-with-lemon-feta.md) — 70 min, 14 servings
- [Mediterranean Roasted Greek Potatoes](recipes/sides/roasted-greek-potatoes.md) — 10 servings — ⚠️ incomplete/unverified
- [Mushroom Risotto](recipes/sides/mushroom-risotto.md) — 50 min, 6 servings
- [No-Fuss Refrigerator Bread & Butter Pickles](recipes/sides/refrigerator-bread-and-butter-pickles.md) — 225 min, 20 servings
- [Roasted Dill Potatoes](recipes/sides/roasted-dill-potatoes.md) — 50 min, 4 servings — ⚠️ incomplete/unverified
- [Shiitake and Broccoli in Soy Garlic Sauce](recipes/sides/shiitake-and-broccoli-in-soy-garlic-sauce.md) — 15 min, 3 servings
- [The Absolute Best Creamed Spinach Recipe Ever](recipes/sides/best-creamed-spinach.md) — 20 min, 4 servings
- [Turmeric Baked Broccoli](recipes/sides/turmeric-baked-broccoli.md) — 35 min, 4 servings — ⚠️ incomplete/unverified

**Soups**
- [Amish Cabbage Soup Recipe With Ground Beef](recipes/soups/amish-cabbage-soup-with-ground-beef.md) — 70 min, 6 servings
- [Brodo di Pollo con Pastina (Italian Chicken Broth with Pastina)](recipes/soups/brodo-di-pollo-con-pastina.md) — 200 min, 6 servings
- [Chicken and Sausage Gumbo (Classic Dark Roux)](recipes/soups/chicken-and-sausage-gumbo-with-dark-roux.md) — 120 min, 6 servings
- [Colombian Chicken Sancocho](recipes/soups/colombian-chicken-sancocho.md) — 50 min, 6 servings
- [Creamy Golden Vegetable Blender Soup](recipes/soups/creamy-golden-vegetable-blender-soup.md) — 45 min, 6 servings
- [Creamy Hungarian Mushroom Soup](recipes/soups/creamy-hungarian-mushroom-soup.md) — 50 min, 6 servings — ⚠️ incomplete/unverified
- [Creamy Spinach and White Bean Soup](recipes/soups/creamy-spinach-and-white-bean-soup.md) — 20 min, 4 servings — ⚠️ incomplete/unverified
- [Easy Chicken & Sausage Gumbo](recipes/soups/chicken-sausage-gumbo.md) — 30 min, 6 servings
- [Hearty Lentil Soup with Chorizo and Spinach](recipes/soups/hearty-lentil-soup-with-chorizo-and-spinach.md) — 75 min, 6 to 8 servings — ⚠️ incomplete/unverified
- [Italian Zuppa di Farro](recipes/soups/italian-zuppa-di-farro.md) — 120 min — ⚠️ incomplete/unverified
- [Lemon Chicken & Rice Soup](recipes/soups/lemon-chicken-rice-soup.md) — 65 min, 4 servings
- [Luxurious Lobster Bisque](recipes/soups/luxurious-lobster-bisque.md) — 80 min, 6 servings — ⚠️ incomplete/unverified
- [Mediterranean Vegetable Soup](recipes/soups/mediterranean-vegetable-soup.md) — 35 min, 6 servings
- [Savory Rotisserie Chicken Broth](recipes/soups/savory-rotisserie-chicken-broth.md) — 125 min, 6 servings — ⚠️ incomplete/unverified
- [Summer Corn Chowder](recipes/soups/summer-corn-chowder.md) — 90 min, 4 servings
- [The Best Swamp Soup](recipes/soups/swamp-soup.md) — 55 min, 8 servings — ⚠️ incomplete/unverified
- [This Simple Hungarian Goulash Recipe Is So Easy to Make (8 Ingredients)](recipes/soups/hungarian-goulash.md) — 140 min, 8 servings
- [Traditional German Potato Soup](recipes/soups/german-potato-soup.md) — 45 min, 4 servings
- [Tuscan White Bean Soup (Minestra di Fagioli)](recipes/soups/tuscan-white-bean-soup.md) — 620 min, 6 servings
- [Ukrainian Mushroom Soup](recipes/soups/ukrainian-mushroom-soup.md) — 40 min, 4 servings — ⚠️ incomplete/unverified
- [Zuppa Toscana (Olive Garden Copycat)](recipes/soups/zuppa-toscana.md) — 45 min, 6 servings

## Flipboard import (in progress)

42 more recipes were added in batch 4 (184 → 226) of converting the ["Food & Flavors" Flipboard magazine](https://flipboard.com/@enetoe/food-flavors-acbn0akgy) (batch 1 added the first 62, batch 2 added 50 more, batch 3 added 56 more — the magazine has about 7,730 saved stories total). Batch 4's yield was lower than earlier batches because a larger share of this pass's candidates came from domains already known to be unreliable from this sandbox (eatingwell.com, simplyrecipes.com, receitas.globo.com) — about half of those still couldn't be recovered even via a browser-based fallback fetch. Roundup/listicle links, non-recipe review articles, confirmed duplicates (including same-dish republishes under a different date path on gamintraveler.com), and pages that stayed unreachable after a retry were intentionally skipped rather than guessed at. See `_build/flipboard-batch-4-report.md` for the full accounting (and the batch 1-3 reports for earlier batches), plus `_cookbook-meta-prompt.md` §6c for the duplicate-detection rule this project runs before every batch. Just say "convert the next batch" to continue with batch 5.

## Quick actions (just ask Claude)
- "Add this recipe: [paste URL or text]"
- "Scale the salmon recipe for 6 people"
- "What can I make with peaches?"
- "Make a shopping list for [recipe names]" (saves a dated file under `shopping-lists/`)
- "Add a note to [recipe] that..."
- "Rebuild the site" (only needed if you edited a recipe file by hand, outside chat)

## Favorites, without asking Claude

Click the star on any recipe card, or the "Add to Favorites" button on a recipe's page, to favorite it. Click **★ Favorites** at the top of the sidebar to browse just your starred recipes — it works like a category filter and combines with search. This lives entirely in the browser (no chat round-trip, no file written) and persists across reloads in the same browser.

## Shopping list, without asking Claude

Open any recipe in `index.html` and click **+ Add to Shopping List**. Click **Shopping List** in the header to see everything you've added, with checkboxes to tick off as you shop. A **By Aisle / By Recipe** toggle at the top controls the grouping — **By Aisle** (the default) sorts everything into grocery-store sections (produce, meat & seafood, dairy, pantry, and so on) so a trip through the store or an online cart only touches each section once, with a small tag on every item showing which recipe it's for; **By Recipe** is the traditional view, grouped under each recipe's name. **Print list** and **Copy to clipboard** both mirror whichever grouping is currently selected, as a simplified, flat checklist with no navigation menu, no card boxes, and no buttons — ready to print to paper/PDF or paste into Word, Notes, or any other app. This lives entirely in the browser (no chat round-trip, no file written) and persists across reloads in the same browser.

## Fixing or completing a recipe, starting from the site

Every recipe page has a **"Fix or complete this recipe"** box at the very bottom. **Open recipe file (.md)** opens that recipe's source Markdown file directly, in case you'd rather edit it yourself. **Copy prompt to paste in chat** copies a ready-made message to your clipboard — pre-filled with the recipe's file path and title — so you can paste it into a Claude chat and just fill in the details; Claude follows §6b of the meta-prompt to merge what you provide and rebuild the site.
