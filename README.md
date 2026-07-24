# Our Cookbook

A Markdown-based personal recipe library with a standalone, searchable HTML browser. See `_cookbook-meta-prompt.md` for the full spec.

## Browse it

Double-click **`index.html`** to open the cookbook site in your browser — no install, no server. Search, filter by category, star a recipe as a favorite and browse just your favorites, open a recipe, and scale servings live.

Every recipe page leads with its description and a compact Prep / Cook / Total / Difficulty box in the top-left corner (any of the four that's missing shows "N.A." rather than being left blank), a clickable source link right below the description, and every card/banner always shows a photo — recipes without their own yet borrow one from another recipe **in the same category only** (never an unrelated dish), clearly labeled as such, or fall back to a plain initials tile if no same-category photo exists either. Clicking a category in the sidebar always shows that category's recipes, even if you'd typed something into the search box first — and the reverse holds too: typing a search keyword always searches every recipe, switching back to "All Recipes" even if a category or ★ Favorites filter was active.

`index.html` is generated from the Markdown files in `recipes/`. It rebuilds automatically whenever you ask Claude to add or edit a recipe. To rebuild it yourself: `python3 _build/build.py`.

## Current recipes

348 recipes across 17 categories. Recipes flagged ⚠️ incomplete/unverified are missing a detail the source didn't state (usually an exact time, servings count, or difficulty) — never a guessed value; open the file's "Missing Information" section to see exactly what's missing, or check the site for the same warning banner (shown at the bottom of the recipe page, below the Print Recipe button).

**Appetizers**
- [Baked Brie with Honey, Walnuts, Figs, and Rosemary](recipes/appetizers/baked-brie-with-the-works.md) — 25 min, 4 servings
- [Burrata with Tomatoes and Pesto](recipes/appetizers/burrata-with-tomatoes-and-pesto.md) — 10 min, 4 servings
- [Crispy Garlic Parmesan Tater Tots](recipes/appetizers/crispy-garlic-parmesan-tater-tots.md) — 30 min, 8 servings — ⚠️ incomplete/unverified
- [Crispy Potato Cheese Croquettes](recipes/appetizers/potato-cheese-croquettes.md) — 50 min — ⚠️ incomplete/unverified
- [Ina Garten's Cauliflower Toast](recipes/appetizers/ina-gartens-cauliflower-toast.md) — details pending — ⚠️ incomplete/unverified
- [Patatas Bravas](recipes/appetizers/patatas-bravas.md) — details pending — ⚠️ incomplete/unverified

**Beef**
- [Boeuf Bourguignon](recipes/beef/boeuf-bourguignon.md) — 360 min, 6 servings — ⚠️ incomplete/unverified
- [Ground Beef Casserole](recipes/beef/ground-beef-and-potato-casserole.md) — 95 min, 6 servings
- [One Pot Creamy Mushroom and Ground Beef Stroganoff](recipes/beef/one-pot-creamy-mushroom-ground-beef-stroganoff.md) — 25 min, 4 servings
- [One-Pan Ground Beef and Vegetables](recipes/beef/one-pan-ground-beef-and-mixed-vegetables.md) — 45 min, 3 servings
- [Spanish Oxtail Stew (Rabo de Toro)](recipes/beef/spanish-oxtail-stew.md) — 270 min, 6 servings
- [Succulent Italian Pot Roast (Stracotto)](recipes/beef/italian-pot-roast-stracotto.md) — 210 min, 8 servings
- [This Perfect Rib Roast Recipe From a Head Chef Is Top Secret](recipes/beef/rib-roast-with-red-wine-jus.md) — 12 servings — ⚠️ incomplete/unverified
- [Fall-Off-the-Bone Braised Short Ribs](recipes/beef/braised-short-ribs-in-red-wine.md) — 195 min, 6 servings
- [Fogo de Chao Picanha (Copycat)](recipes/beef/fogo-de-chao-picanha.md) — 35 min, 8 servings
- [Garlic Butter Bacon Cheeseburger](recipes/beef/garlic-butter-bacon-cheeseburger.md) — 150 min, 4 servings
- [Homemade Salisbury Steak](recipes/beef/salisbury-steak.md) — 40 min, 4 servings
- [Juicy Beef Steak Tips with Rich Mushroom Gravy](recipes/beef/juicy-beef-steak-tips-with-mushroom-gravy.md) — 45 min, 4 servings
- [Maminha com Manteiga Temperada](recipes/beef/maminha-com-manteiga-temperada.md) — 60 min, 5 servings — ⚠️ incomplete/unverified
- [Shortcut Budget Beef Tips With Savory Brown Gravy](recipes/beef/budget-beef-tips-with-brown-gravy.md) — 130 min, 8 servings — ⚠️ incomplete/unverified
- [Pan-Seared Rib-Eye With Mushroom-Hunter's Sauce](recipes/beef/pan-seared-rib-eye-mushroom-hunters-sauce.md) — 60 min, 2 servings

**Beverages**
- [Boba Tea (Basic Recipe)](recipes/beverages/boba-tea.md) — 25 min, 2 servings
- [Easy Homemade Watermelon Lemonade](recipes/beverages/watermelon-lemonade.md) — 10 min — ⚠️ incomplete/unverified
- [Fresh Lemon Cucumber Mint Water](recipes/beverages/lemon-cucumber-mint-water.md) — 5 min — ⚠️ incomplete/unverified
- [Lemon Cucumber Mint Infused Water](recipes/beverages/lemon-cucumber-mint-infused-water.md) — 490 min, 6 servings — ⚠️ incomplete/unverified
- [Vanilla Chai Protein Smoothie](recipes/beverages/vanilla-chai-protein-smoothie.md) — 5 min, 2 servings
- [Whipped Strawberry Lemonade](recipes/beverages/whipped-strawberry-lemonade.md) — 70 min, 4 servings
- [Brazilian Lemonade](recipes/beverages/brazilian-lemonade.md) — details pending — ⚠️ incomplete/unverified
- [Caipirinha](recipes/beverages/caipirinha.md) — 5 min, 1 serving

**Breads**
- [Focaccia](recipes/breads/focaccia.md) — "240" min, 8 servings
- [One Dough, Four Breads Europeans Actually Eat On Weeknights](recipes/breads/one-dough-four-breads.md) — 120 min, 10 servings
- [Amish Cornbread](recipes/breads/amish-cornbread.md) — 27 min, 9 servings
- [Cheese Bread (Pão de Queijo style)](recipes/breads/cheese-bread.md) — details pending — ⚠️ incomplete/unverified
- [Cheesy Hawaiian Garlic Rolls](recipes/breads/cheesy-hawaiian-garlic-rolls.md) — 15 min, 9 servings
- [Easy Georgian Cheese Bread (Adjarian Khachapuri)](recipes/breads/adjarian-khachapuri.md) — 60 min, 12 servings
- [Homemade Naan](recipes/breads/homemade-naan.md) — 90 min, 8 servings
- [Nonna's No-Knead Pizza Dough](recipes/breads/no-knead-pizza-dough.md) — 30 min, 16 servings
- [Savory Mediterranean Spinach Feta Loaf](recipes/breads/mediterranean-spinach-feta-loaf.md) — 70 min, 10 servings
- [Whole-Loaf Cheesy Garlic Bread](recipes/breads/whole-loaf-cheesy-garlic-bread.md) — 4-8 servings — ⚠️ incomplete/unverified
- [No-Knead Olive Cheese Bread](recipes/breads/no-knead-olive-cheese-bread.md) — 290 min, makes 1 loaf

**Breakfast**
- [Creamy Applesauce Oatmeal](recipes/breakfast/creamy-applesauce-oatmeal.md) — 5 min, 1 servings
- [Apricot-Pistachio Overnight Oats](recipes/breakfast/apricot-pistachio-overnight-oats.md) — 495 min, 4 servings — ⚠️ incomplete/unverified
- [Avocado Toast Three Ways](recipes/breakfast/avocado-toast-three-ways.md) — 20 min, 8 servings
- [Cheesy Baked Polenta and Egg with Bacon](recipes/breakfast/cheesy-baked-polenta-and-egg-with-bacon.md) — 40 min, 2 servings
- [High-Protein Mediterranean Egg Casserole](recipes/breakfast/high-protein-mediterranean-egg-casserole.md) — "45 to 50" min, 8 servings
- [Honey Nut Granola](recipes/breakfast/honey-nut-granola.md) — 50 min, 8 servings
- [Zucchini and Eggs Skillet Recipe](recipes/breakfast/zucchini-and-eggs-skillet.md) — 30 min, 2 servings

**Desserts**
- [Amazing Pecan Pie Cake](recipes/desserts/pecan-pie-cake.md) — 70 min, 12 servings
- [Creamy Key Lime Pie with Buttery Graham Cracker Crust](recipes/desserts/key-lime-pie.md) — 45 min, 8 servings
- [Ina Garten's Blueberry Ricotta Cake Recipe Is a Slice of Heaven](recipes/desserts/blueberry-ricotta-cake.md) — 70 min, 8 servings
- [Tiramisu](recipes/desserts/tiramisu.md) — details pending — ⚠️ incomplete/unverified
- [Apple Crunch Cheesecake](recipes/desserts/apple-crunch-cheesecake.md) — 90 min, 8 servings
- [Bisquick Apple Cobbler](recipes/desserts/bisquick-apple-cobbler.md) — 50 min, 6 servings
- [Buttery Bread Pudding With Bourbon Butter Sauce](recipes/desserts/buttery-bread-pudding-with-bourbon-butter-sauce.md) — 75 min, 12 servings
- [Creamy Pineapple Sherbet](recipes/desserts/creamy-pineapple-sherbet.md) — 160 min, 4 servings — ⚠️ incomplete/unverified
- [Creamy Pumpkin Cheesecake Mousse](recipes/desserts/creamy-pumpkin-cheesecake-mousse.md) — 10 min, 6 servings
- [Date and Walnut Cake](recipes/desserts/date-and-walnut-cake.md) — 60 min, 8 servings
- [Homemade Pistachio Cannoli](recipes/desserts/homemade-pistachio-cannoli.md) — 135 min, 8 servings
- [Italian Lemon Cream Cake](recipes/desserts/italian-lemon-cream-cake.md) — 60 min, 8 servings — ⚠️ incomplete/unverified
- [Julie Andrews' Carrot Cake](recipes/desserts/julie-andrews-carrot-cake.md) — 8 servings — ⚠️ incomplete/unverified
- [Limoncello Bundt Cake](recipes/desserts/limoncello-bundt-cake.md) — details pending — ⚠️ incomplete/unverified
- [Limoncello Tiramisu](recipes/desserts/limoncello-tiramisu.md) — 265 min, 12 servings
- [Luscious Lemon Ricotta Cake](recipes/desserts/lemon-ricotta-cake.md) — 60 min, 10 servings
- [Matthew McConaughey's Favorite No-Bake Lemon Cheesecake](recipes/desserts/no-bake-lemon-cheesecake.md) — 15 min, 8 servings
- [No-Bake Boston Cream Pie Bars](recipes/desserts/no-bake-boston-cream-pie-bars.md) — details pending — ⚠️ incomplete/unverified
- [Peanut Butter Fandango Rice Krispies Treats](recipes/desserts/peanut-butter-fandango-rice-krispies-treats.md) — 30 min, 12 servings
- [Pumpkin Pie Dessert Bars](recipes/desserts/pumpkin-pie-dessert-bars.md) — 70 min, 16 servings
- [Rabanada da Solange Couto](recipes/desserts/rabanada-da-solange-couto.md) — 30 min, 10 servings
- [Sourdough Carrot Cake Muffins](recipes/desserts/sourdough-carrot-cake-muffins.md) — 30 min — ⚠️ incomplete/unverified
- [Spooky Sweet Potato Ghost Hand Pies](recipes/desserts/spooky-sweet-potato-ghost-hand-pies.md) — 80 min, 16 servings
- [Swedish Apple Cake](recipes/desserts/swedish-apple-cake.md) — 60 min, 8 servings — ⚠️ incomplete/unverified
- [Warm Peach Cake](recipes/desserts/warm-peach-cake.md) — 12 servings — ⚠️ incomplete/unverified
- [Baked Bananas in Brown Sugar](recipes/desserts/baked-bananas-in-brown-sugar.md) — details pending — ⚠️ incomplete/unverified
- [Banana Bread Crumb Cake](recipes/desserts/banana-bread-crumb-cake.md) — details pending
- [Bourbon Chocolate Derby Pie](recipes/desserts/bourbon-chocolate-derby-pie.md) — 50 min, 8 servings
- [Lemon-Blueberry Trifle](recipes/desserts/lemon-blueberry-trifle.md) — 225 min, 12 servings
- [Peanut Butter Spider Cookies](recipes/desserts/peanut-butter-spider-cookies.md) — 40 min, 16 servings

**Dips & Spreads**
- [Authentic Restaurant-Style Italian Bread Dipping Oil](recipes/dips-spreads/italian-bread-dipping-oil.md) — 5 min, 20 servings
- [Avocado Hummus](recipes/dips-spreads/avocado-hummus.md) — 15 min, 6 servings
- [Beet Hummus](recipes/dips-spreads/beet-hummus.md) — 50 min, 6 servings
- [Chocolate Brownie Batter Hummus](recipes/dips-spreads/chocolate-brownie-batter-hummus.md) — 65 min, 12 servings
- [Creamy Black-Eyed Pea Hummus](recipes/dips-spreads/black-eyed-pea-hummus.md) — 7 min, 6 servings
- [Mexican-Style Black Bean Hummus](recipes/dips-spreads/mexican-style-black-bean-hummus.md) — 15 min, 6 servings
- [Pineapple Serrano Hummus](recipes/dips-spreads/pineapple-serrano-hummus.md) — details pending — ⚠️ incomplete/unverified
- [Roasted Carrot Hummus](recipes/dips-spreads/roasted-carrot-hummus.md) — 33 min, 6 servings
- [Roasted Red Pepper Hummus](recipes/dips-spreads/roasted-red-pepper-hummus.md) — 25 min, 6 servings
- [Smooth Garlic Hummus (Israeli-Style)](recipes/dips-spreads/smooth-garlic-hummus.md) — 165 min, 4 servings
- [Spicy Harissa Hummus](recipes/dips-spreads/harissa-hummus.md) — 5 min, 6 servings
- [Sweet Potato Hummus](recipes/dips-spreads/sweet-potato-hummus.md) — 30 min, 4 servings
- [Tzatziki Recipe](recipes/dips-spreads/tzatziki-xoxobella.md) — 75 min, 4 servings — ⚠️ incomplete/unverified
- [White Bean Hummus with Feta](recipes/dips-spreads/white-bean-hummus-feta.md) — 10 min, 6 servings
- [Zucchini Hummus](recipes/dips-spreads/zucchini-hummus.md) — 5 min, 8 servings
- [Blue Cheese Dressing](recipes/dips-spreads/blue-cheese-dressing.md) — 8 min, 12 servings
- [Mediterranean Cream Cheese Dip](recipes/dips-spreads/mediterranean-cream-cheese-dip.md) — 15 min, 4 servings
- [Mediterranean Lemon Basil Vinaigrette](recipes/dips-spreads/lemon-basil-vinaigrette.md) — 10 min, 8 servings — ⚠️ incomplete/unverified
- [Muffuletta Dip](recipes/dips-spreads/muffuletta-dip.md) — 60 min, 10-12 servings
- [Tzatziki](recipes/dips-spreads/tzatziki.md) — details pending — ⚠️ incomplete/unverified

**Meat Mains**
- [The Best Meatballs Ever! (Italian Polpette Recipe)](recipes/meat-mains/polpette-italian-meatballs-in-tomato-sauce.md) — 55 min, "4-6" servings
- [Abbacchio al Forno (Italian Roast Lamb)](recipes/meat-mains/abbacchio-al-forno-roast-lamb.md) — details pending — ⚠️ incomplete/unverified
- [Costolette di Maiale ai Funghi (Pork Chops with Mushroom Cream Sauce)](recipes/meat-mains/pork-chops-with-mushroom-cream-sauce.md) — 60 min, 4 servings — ⚠️ incomplete/unverified
- [Cotoletta alla Milanese](recipes/meat-mains/cotoletta-alla-milanese.md) — 4 servings — ⚠️ incomplete/unverified
- [Herb Crusted Pork Tenderloin With Mushroom Gravy](recipes/meat-mains/herb-crusted-pork-tenderloin-with-mushroom-gravy.md) — 30 min, 6 servings
- [Lamb Loin Chops](recipes/meat-mains/lamb-loin-chops.md) — 25 min, 3 servings
- [Porchetta](recipes/meat-mains/porchetta.md) — details pending — ⚠️ incomplete/unverified
- [Sausage Stuffed Butternut Squash](recipes/meat-mains/sausage-stuffed-butternut-squash.md) — 60 min, 2 servings
- [Slow Cooker Lamb Shanks With Red Wine Gravy](recipes/meat-mains/slow-cooker-lamb-shanks-with-red-wine-gravy.md) — 530 min, 2 servings
- [Batata Rosti com Carne-Seca](recipes/meat-mains/batata-rosti-com-carne-seca.md) — 60 min, 4 servings

**Pasta**
- [$1000 Baked Spaghetti Pasta Casserole](recipes/pasta/1000-baked-spaghetti-pasta-casserole.md) — 50 min, 6 servings
- [Authentic Spaghetti Carbonara](recipes/pasta/spaghetti-carbonara.md) — details pending — ⚠️ incomplete/unverified
- [Canned Tuna Pasta](recipes/pasta/canned-tuna-pasta.md) — 30 min, 6 servings
- [Cheesy Italian Penne Pasta with Sundried Tomatoes](recipes/pasta/cheesy-italian-penne-pasta-with-sundried-tomatoes.md) — 15 min, 4 servings
- [Creamy Cajun Sausage Spaghetti](recipes/pasta/creamy-cajun-sausage-spaghetti.md) — 40 min, 2 servings — ⚠️ incomplete/unverified
- [Creamy Lemon Pasta (Pasta al Limone)](recipes/pasta/creamy-lemon-pasta.md) — 30 min, 4 servings
- [Creamy Lemon Ricotta Pasta](recipes/pasta/creamy-lemon-ricotta-pasta.md) — 15 min, 4 servings
- [Fabulous Fettuccine Recipe With Creamy Mushroom Sauce](recipes/pasta/fabulous-fettuccine-with-creamy-mushroom-sauce.md) — 25 min, 4 servings
- [Light Shrimp Feta Pasta Recipe Is Ready In a Flash & High Protein (20 Minutes)](recipes/pasta/lemony-shrimp-feta-pasta.md) — 20 min, 4 servings
- [Pasta al Limón (Lemon Carbonara)](recipes/pasta/pasta-al-limon.md) — 20 min, 6 servings
- [Prisoner's Pasta (Pasta alla Carcerata)](recipes/pasta/prisoners-pasta.md) — 27 min, 3 servings
- [Spinach Artichoke Stuffed Shells](recipes/pasta/spinach-artichoke-stuffed-shells.md) — 45 min, 8 servings
- [Tagliatelle al Ragù](recipes/pasta/tagliatelle-al-ragu.md) — "180-300" min, 4 servings — ⚠️ incomplete/unverified
- [The Godfather's Sunday Gravy](recipes/pasta/godfathers-sunday-gravy.md) — 10 servings — ⚠️ incomplete/unverified
- [This Creamy Lemon Rigatoni Is All I'm Making This Week for Dinner](recipes/pasta/creamy-lemon-cottage-cheese-rigatoni.md) — 30 min, 6 servings — ⚠️ incomplete/unverified
- [Artichoke Pesto Pasta](recipes/pasta/artichoke-pesto-pasta.md) — 25 min, 4 servings
- [Authentic Spaghetti Bolognese](recipes/pasta/authentic-spaghetti-bolognese.md) — 80 min, 4 servings
- [BLT Carbonara](recipes/pasta/blt-carbonara.md) — 40 min, 4 servings
- [Cherry Tomato & Feta Pasta](recipes/pasta/cherry-tomato-feta-pasta.md) — 55 min, 4 servings
- [Creamy Boursin Orzo with Spinach](recipes/pasta/creamy-boursin-orzo-with-spinach.md) — 15 min, 6 servings
- [Creamy Boursin Pasta With Roasted Vegetables & Chicken](recipes/pasta/creamy-boursin-pasta-with-roasted-vegetables-chicken.md) — 50 min, 6 servings — ⚠️ incomplete/unverified
- [Creamy Corn Orzo](recipes/pasta/creamy-corn-orzo.md) — 4 servings — ⚠️ incomplete/unverified
- [Creamy Feta & Tomato Pasta](recipes/pasta/creamy-feta-tomato-pasta.md) — 30 min, 4 servings
- [Creamy Garlic Parmesan Orzo](recipes/pasta/creamy-garlic-parmesan-orzo.md) — 20 min, 6 servings
- [Creamy Greek Spinach Orzo with Feta](recipes/pasta/creamy-greek-spinach-orzo-with-feta.md) — 30 min, 4 servings
- [Creamy Ground Beef Alfredo Pasta](recipes/pasta/creamy-ground-beef-alfredo-pasta.md) — 20 min, 6 servings
- [Creamy Ricotta Pesto Pasta](recipes/pasta/creamy-ricotta-pesto-pasta.md) — 20 min, 6 servings
- [Creamy Spinach Artichoke Pasta Casserole](recipes/pasta/creamy-spinach-artichoke-pasta-casserole.md) — 35 min, 6 servings — ⚠️ incomplete/unverified
- [Easy Gnocchi Alla Vodka With Burrata](recipes/pasta/gnocchi-alla-vodka-with-burrata.md) — 41 min, 4 servings
- [Fettuccine Alfredo (Roman-Style)](recipes/pasta/fettuccine-alfredo.md) — 20 min — ⚠️ incomplete/unverified
- [Pasta alla Norma](recipes/pasta/pasta-alla-norma.md) — details pending — ⚠️ incomplete/unverified
- [Quick Italian Sausage Pasta with Tomato Cream Sauce](recipes/pasta/quick-italian-sausage-pasta-with-tomato-cream-sauce.md) — 20 min, 5 servings
- [Sausage-Broccoli Pasta](recipes/pasta/sausage-broccoli-pasta.md) — details pending — ⚠️ incomplete/unverified
- [Sheet-Pan Garlic-Butter Gnocchi With Summer Vegetables](recipes/pasta/sheet-pan-garlic-butter-gnocchi-with-summer-vegetables.md) — 40 min, 4 servings — ⚠️ incomplete/unverified
- [Short Rib Pappardelle](recipes/pasta/short-rib-pappardelle.md) — 200-230 min, 6-8 servings
- [Sizzling Spaghetti](recipes/pasta/sizzling-spaghetti.md) — details pending — ⚠️ incomplete/unverified
- [Spaghetti Aglio e Olio](recipes/pasta/spaghetti-aglio-e-olio.md) — 15 min, 2 servings — ⚠️ incomplete/unverified
- [Spaghetti alla Puveriello (Poor Man's Spaghetti)](recipes/pasta/spaghetti-alla-puveriello-poor-mans-spaghetti.md) — 25 min, 2 servings
- [Spinach with Fettuccine](recipes/pasta/fettuccine-and-spinach.md) — 20 min, 4 servings
- [Spinach-And-Sun-Dried Tomato Pasta](recipes/pasta/spinach-sun-dried-tomato-pasta-with-chicken.md) — 20 min, "6-8" servings
- [Tagliatelle al Limone (Lemon Sauce)](recipes/pasta/tagliatelle-al-limone.md) — details pending — ⚠️ incomplete/unverified
- [Tagliatelle al Tartufo Truffle Sauce](recipes/pasta/tagliatelle-al-tartufo-truffle-sauce.md) — 30 min, 4 servings
- [Tomato Cottage Cheese Pasta Sauce](recipes/pasta/tomato-cottage-cheese-pasta-sauce.md) — 20 min, 4 servings — ⚠️ incomplete/unverified
- [Tortellini With Bacon And Peas](recipes/pasta/tortellini-with-bacon-and-peas.md) — 30 min, 4 to 6 servings

**Poultry**
- [Bahrain Spiced Chicken & Rice (Chicken Machboos)](recipes/poultry/bahrain-chicken-machboos.md) — 75 min, 4 servings — ⚠️ incomplete/unverified
- [Coq au Vin](recipes/poultry/coq-au-vin.md) — 100 min, 6 servings
- [Easy Broccoli Cashew Chicken Stir Fry](recipes/poultry/broccoli-cashew-chicken-stir-fry.md) — 30 min, 6 servings
- [Frango com Quiabo e Polenta (Chicken with Okra and Polenta)](recipes/poultry/frango-com-quiabo-e-polenta.md) — 90 min — ⚠️ incomplete/unverified
- [Healthier Creamy Tuscan Chicken (Slow Cooker or Instant Pot)](recipes/poultry/healthier-creamy-tuscan-chicken-slow-cooker-instant-pot.md) — 6 servings
- [Nonna's Sundried Tomato Italian Chicken](recipes/poultry/nonnas-sundried-tomato-italian-chicken.md) — 190 min, 8 servings — ⚠️ incomplete/unverified
- [Apple Cider Chicken Thighs](recipes/poultry/apple-cider-chicken-thighs.md) — 40 min, 4 servings
- [Baked Chicken Lombardy](recipes/poultry/baked-chicken-lombardy.md) — 35 min, 4 servings
- [Chicken Stir Fry With Vegetables](recipes/poultry/chicken-stir-fry-with-vegetables.md) — 25 min, 4 servings
- [Classic Creamy Tuscan Chicken](recipes/poultry/classic-creamy-tuscan-chicken.md) — 40 min, 4 servings
- [Easy Cassoulet](recipes/poultry/easy-cassoulet.md) — 75 min, 4 servings
- [Garlic Butter Baked Parmesan Chicken](recipes/poultry/garlic-butter-baked-parmesan-chicken.md) — 35 min, 4 servings
- [Grilled Ginger Chicken With Charred Peaches](recipes/poultry/grilled-ginger-chicken-with-charred-peaches.md) — "30 to 35" min, 6 servings
- [Homemade Chicken Tikka Masala](recipes/poultry/homemade-chicken-tikka-masala.md) — 90 min, 4 servings
- [Juicy Greek Chicken](recipes/poultry/juicy-greek-chicken.md) — 85 min, 6 servings
- [Juicy Sauteed Chicken Breast](recipes/poultry/juicy-sauteed-chicken-breast.md) — 33 min, 4 servings
- [Lemon Pepper Baked Chicken Drumsticks](recipes/poultry/lemon-pepper-baked-chicken-drumsticks.md) — 40 min, 6 servings
- [Magic Mayo Parmesan Baked Chicken](recipes/poultry/magic-mayo-parmesan-baked-chicken.md) — 25 min, 4 servings
- [Mediterranean Sausage and White Bean Skillet](recipes/poultry/mediterranean-sausage-white-bean-skillet.md) — 25 min, 2 to 4 servings — ⚠️ incomplete/unverified
- [Savory Slow Cooker Mediterranean Balsamic Chicken](recipes/poultry/savory-slow-cooker-mediterranean-balsamic-chicken.md) — 240 min, 8 servings
- [Shortcut French Chicken](recipes/poultry/french-chicken.md) — 6 servings — ⚠️ incomplete/unverified
- [Wine Chicken](recipes/poultry/wine-chicken.md) — 35 min, "4 to 6" servings
- [Chicken Thigh Marsala](recipes/poultry/chicken-thigh-marsala.md) — details pending

**Salads**
- [Asparagus Salad](recipes/salads/asparagus-salad.md) — 15 min, 6 servings
- [Balsamic Spinach Strawberry Feta Salad with Walnuts](recipes/salads/balsamic-spinach-strawberry-feta-salad-with-walnuts.md) — 8 min, 3 servings
- [Chickpea, Beet & Cucumber Salad](recipes/salads/chickpea-beet-cucumber-salad.md) — 20 min, 6 servings — ⚠️ incomplete/unverified
- [High-Fiber Chickpea & Farro Salad with Artichokes & Tomatoes](recipes/salads/chickpea-farro-salad-with-artichokes-and-tomatoes.md) — 20 min, 8 servings
- [Ina Garten's Creamy Potato Salad](recipes/salads/ina-gartens-creamy-potato-salad.md) — "30-35" min, 8 servings
- [Lilo's Authentic German Potato Salad](recipes/salads/lilos-authentic-german-potato-salad.md) — 40 min, 12 servings
- [Mediterranean Lemony Lentil Salad (Gluten-Free, Low-Sodium, Low-Calorie)](recipes/salads/mediterranean-lemony-lentil-salad.md) — 30 min, 8 servings
- [Napa Valley Avocado & Corn Salad with Creamy Feta Dressing](recipes/salads/napa-valley-avocado-corn-salad.md) — 30 min, 6 servings
- [Niçoise Salad](recipes/salads/nicoise-salad.md) — 30 min, 8 servings — ⚠️ incomplete/unverified
- [Tuna Nicoise Salad](recipes/salads/tuna-nicoise-salad.md) — 35 min, 2 servings
- [5-Minute Greek Salad (Maroulosalata)](recipes/salads/5-minute-greek-salad-maroulosalata.md) — 5 min, 4-6 servings
- [Apple Cranberry Slaw](recipes/salads/apple-cranberry-slaw.md) — 20 min, 8 servings
- [Asparagus and Pea Salad](recipes/salads/asparagus-and-pea-salad.md) — 20 min, 4 servings
- [Bavarian Potato Salad](recipes/salads/bavarian-potato-salad.md) — 15 min, 4 servings
- [Beet and Feta Salad with Pistachios and Pears](recipes/salads/beet-and-feta-salad-with-pistachios-and-pears.md) — 15 min, 2 servings
- [Beet Salad with Feta](recipes/salads/beet-salad-with-feta-and-mandarin-oranges.md) — 70 min, 4 servings
- [Crab Salad](recipes/salads/crab-salad.md) — 15 min, 6 servings
- [Creamy Amish Cucumber Salad](recipes/salads/creamy-amish-cucumber-salad.md) — 10 min, 6 servings
- [Creamy Green Bean Potato Salad With Avocado Dressing](recipes/salads/green-bean-potato-salad-with-avocado-dressing.md) — 50 min, 8 servings — ⚠️ incomplete/unverified
- [Creamy Mediterranean White Bean Salad](recipes/salads/mediterranean-white-bean-salad.md) — 20 min, 8 servings
- [Cucumber Dill Salad](recipes/salads/cucumber-dill-salad.md) — 10 min — ⚠️ incomplete/unverified
- [Cucumber Salad](recipes/salads/creamy-cucumber-salad.md) — 70 min, 4 servings
- [Cucumber Salad with Herbs and Pine Nuts](recipes/salads/cucumber-salad-with-herbs-and-pine-nuts.md) — 10 min, 6 servings
- [Dill Pickle Ranch Potato Salad](recipes/salads/dill-pickle-ranch-potato-salad.md) — 110 min, 12 servings — ⚠️ incomplete/unverified
- [Festive Watermelon Salad with Feta](recipes/salads/festive-watermelon-salad-with-feta.md) — 10 min, 10 servings
- [French Bistro Salad with Punchy Dijon Vinaigrette](recipes/salads/french-bistro-salad-with-dijon-vinaigrette.md) — 10 min, 4 servings
- [French Lentil Salad](recipes/salads/french-lentil-salad.md) — 35 min, 6 servings
- [Goat Cheese Salad With Green Beans](recipes/salads/goat-cheese-salad-with-green-beans.md) — 4 servings
- [Greek Pasta Salad](recipes/salads/greek-pasta-salad.md) — 20 min, 8 servings
- [Greek Salmon Salad](recipes/salads/greek-salmon-salad.md) — 25 min, 6 servings
- [Greek Tuna Stuffed Avocados](recipes/salads/greek-tuna-stuffed-avocados.md) — 10 min, 2 servings
- [High-Fiber Cucumber Avocado Salad](recipes/salads/cucumber-avocado-salad.md) — 10 min, 6 servings — ⚠️ incomplete/unverified
- [High-Protein Caprese Salad](recipes/salads/high-protein-caprese-salad.md) — 5 min, 2 servings — ⚠️ incomplete/unverified
- [High-Protein No-Mayonnaise Tuna Salad](recipes/salads/high-protein-no-mayonnaise-tuna-salad.md) — 10 min, 3 servings
- [Italian Tuna Potato Salad](recipes/salads/italian-tuna-potato-salad.md) — 25 min, 4 servings
- [Lemon-Garlic Dense Bean Salad with Feta](recipes/salads/lemon-garlic-dense-bean-salad-with-feta.md) — 20 min, 4 servings — ⚠️ incomplete/unverified
- [Matthew McConaughey's Tuna Salad](recipes/salads/matthew-mcconaughey-tuna-salad.md) — 16 min — ⚠️ incomplete/unverified
- [Mediterranean Chickpea Cucumber Salad](recipes/salads/mediterranean-chickpea-cucumber-salad.md) — 15 min, 6 servings
- [Mediterranean Potato Salad With Smashed Olives and Mint](recipes/salads/mediterranean-potato-salad-with-smashed-olives-and-mint.md) — 30 min, 10 servings
- [Mediterranean White Bean Salad with Feta](recipes/salads/mediterranean-white-bean-salad-with-feta.md) — 40 min, 4 servings
- [Melon Tomato Salad](recipes/salads/melon-tomato-salad.md) — 20 min, "6-8" servings
- [Mexican Street Corn-Inspired Bean Salad](recipes/salads/mexican-street-corn-inspired-bean-salad.md) — 10 min, 6 servings
- [Peach Blueberry Cucumber Salad with Feta in Lemon Basil Vinaigrette](recipes/salads/peach-blueberry-cucumber-salad-with-feta.md) — 15 min, 6 servings
- [Radish Salad](recipes/salads/radish-salad.md) — 4 servings — ⚠️ incomplete/unverified
- [Red Potato Salad](recipes/salads/red-potato-salad.md) — 6 servings
- [Roasted Eggplant and Chickpea Buddha Bowl](recipes/salads/roasted-eggplant-and-chickpea-buddha-bowl.md) — 20 min, 2 servings
- [Roasted Potato Tzatziki Bowls](recipes/salads/roasted-potato-tzatziki-bowls.md) — 45 min, 4 servings
- [Salada de grão-de-bico com cebola marinada](recipes/salads/chickpea-salad-with-marinated-onion.md) — 30 min, 6 servings
- [Seafood Pasta Salad](recipes/salads/seafood-pasta-salad.md) — 78 min, 6 servings
- [Simple Is Best Arugula Salad](recipes/salads/simple-is-best-arugula-salad.md) — 15 min, 8 servings
- [Strawberry Spinach Salad with Fresh Oranges](recipes/salads/strawberry-spinach-salad-with-fresh-oranges.md) — 10 min, 4 servings
- [Thanksgiving Slaw](recipes/salads/thanksgiving-slaw.md) — 15 min, 8 servings — ⚠️ incomplete/unverified
- [Three Bean Salad](recipes/salads/three-bean-salad.md) — 25 min, 8 servings
- [Tortellini Pasta Salad](recipes/salads/tortellini-pasta-salad.md) — 20 min, 8 servings
- [Watermelon Feta Salad with Honey Lime Dressing](recipes/salads/watermelon-feta-salad-with-honey-lime-dressing.md) — 15 min, 4 servings
- [Watermelon Panzanella Salad](recipes/salads/watermelon-panzanella-salad.md) — 24 min, 4 servings
- [Zesty Lemon Dill Tuna Salad](recipes/salads/zesty-lemon-dill-tuna-salad.md) — 1 servings — ⚠️ incomplete/unverified

**Sandwiches**
- [Italian Panini Sandwich](recipes/sandwiches/italian-panini-sandwich.md) — 2 servings — ⚠️ incomplete/unverified
- [Tyler Smith's French Bread Pizza](recipes/sandwiches/french-bread-pizza.md) — 30 min, 4 servings
- [Cheddar Tomato Sandwich, a Tomato Farmer's Method](recipes/sandwiches/cheddar-tomato-sandwich-farmers-method.md) — 1 servings — ⚠️ incomplete/unverified
- [Chickpea Salad Sandwich](recipes/sandwiches/chickpea-salad-sandwich.md) — 15 min, "3 to 4 sandwiches" servings
- [Ham and Cheese Toast (4 Ingredients)](recipes/sandwiches/ham-and-cheese-toast.md) — 6 min, 2 servings — ⚠️ incomplete/unverified
- [Marv 'n' Joe Tomato Sandwich](recipes/sandwiches/marv-n-joe-tomato-sandwich.md) — 2 servings — ⚠️ incomplete/unverified

**Sauces**
- [Sugo della Nonna: Italian Sunday Tomato Sauce](recipes/sauces/sugo-della-nonna-italian-sunday-tomato-sauce.md) — "120-150" min, "4-6" servings
- [Classic Bolognese Sauce](recipes/sauces/classic-bolognese-sauce.md) — 160 min, 4 servings
- [Richard and Suzanne's Famous Spaghetti Sauce](recipes/sauces/richard-and-suzannes-spaghetti-sauce.md) — 25 min, 6 servings — ⚠️ incomplete/unverified
- [Fermented Garlic With Honey](recipes/sauces/fermented-garlic-with-honey.md) — 20 min, 40 servings

**Sauces & Dressings**
- [Lebanese Salad Dressing](recipes/sauces-dressings/lebanese-salad-dressing.md) — 4 min, "1 cup" servings
- [Lemon-Dill Vinaigrette](recipes/sauces-dressings/lemon-dill-vinaigrette.md) — 5 min, 6 servings — ⚠️ incomplete/unverified
- [Sugar Free Honey Lime Dressing](recipes/sauces-dressings/sugar-free-honey-lime-dressing.md) — 5 min, 8 servings
- [5-Minute Homemade French Salad Dressing](recipes/sauces-dressings/everyday-french-vinaigrette.md) — 5 min
- [Garlic-Dijon Vinaigrette](recipes/sauces-dressings/garlic-dijon-vinaigrette.md) — 10 min, 16 servings
- [Avocado Cilantro Dressing](recipes/sauces-dressings/avocado-cilantro-dressing.md) — 10 min, 4 servings

**Seafood Mains**
- [Bacalhau da Amizade (Brandade de Bacalhau) do Claude Troisgros](recipes/seafood-mains/bacalhau-da-amizade-brandade.md) — 60 min, 4 servings
- [Back-to-Basics: How to Make Salmon on the Griddle](recipes/seafood-mains/griddled-salmon.md) — details pending — ⚠️ incomplete/unverified
- [Blackened Halibut With Mango-Avocado Relish](recipes/seafood-mains/blackened-halibut-with-mango-avocado-relish.md) — 18 min, 2 servings
- [Creamy Garlic Shrimp Recipe Is the Best Thing You'll Eat All Week (20 Minutes, 7 Ingredients)](recipes/seafood-mains/creamy-garlic-shrimp.md) — 20 min, 6 servings
- [Easy 1-Pan Garlic Shrimp and Ramen Noodles](recipes/seafood-mains/garlic-shrimp-ramen-noodles.md) — 30 min, 4 servings
- [5-Ingredient Honey Garlic Glazed Salmon](recipes/seafood-mains/honey-garlic-glazed-salmon.md) — 22 min, 4 servings
- [Bacalao a la Vizcaína](recipes/seafood-mains/bacalao-a-la-vizcaina.md) — details pending — ⚠️ incomplete/unverified
- [Bacalhau ao forno com batatas e azeitonas pretas](recipes/seafood-mains/bacalhau-ao-forno-com-batatas-e-azeitonas-pretas.md) — 60 min, 6 servings
- [Bacalhau com Batata do Claude Troisgros](recipes/seafood-mains/bacalhau-com-batata-do-claude-troisgros.md) — 4 servings
- [Bacalhau com Batatas ao Murro](recipes/seafood-mains/bacalhau-com-batatas-ao-murro.md) — 4 servings
- [Bacalhau à Brás](recipes/seafood-mains/bacalhau-a-bras.md) — 2220 min, "4 as an appetizer, 2 as a main course" servings — ⚠️ incomplete/unverified
- [Bacalhau à Lagareiro do Claude Troisgros](recipes/seafood-mains/bacalhau-a-lagareiro.md) — 180 min, 8 servings
- [Baked Halibut](recipes/seafood-mains/baked-halibut.md) — 25 min, 4 servings
- [Buttery Garlic Lemon Shrimp](recipes/seafood-mains/buttery-garlic-lemon-shrimp.md) — 10 min, 4 servings
- [Cedar Plank Salmon](recipes/seafood-mains/cedar-plank-salmon.md) — details pending — ⚠️ incomplete/unverified
- [Cider-Glazed Salmon](recipes/seafood-mains/cider-glazed-salmon.md) — 30 min, 2 servings
- [Crunchy Ranch Pan-fried Tilapia Recipe](recipes/seafood-mains/crunchy-ranch-pan-fried-tilapia.md) — 15 min, 4 servings
- [Gambas al Ajillo (Spanish Garlic Shrimp)](recipes/seafood-mains/gambas-al-ajillo.md) — details pending — ⚠️ incomplete/unverified
- [Garlic Knot Salmon](recipes/seafood-mains/garlic-knot-salmon.md) — 24 min, 4 servings
- [Lemon-Garlic Salmon & Broccoli Bowls](recipes/seafood-mains/lemon-garlic-salmon-broccoli-bowls.md) — 30 min, 4 servings
- [Linguine with Clams, Cherry Tomatoes, and Capers](recipes/seafood-mains/linguine-with-clams-cherry-tomatoes-and-capers.md) — 45 min, 4 servings — ⚠️ incomplete/unverified
- [Marmitako (Basque Tuna and Potato Stew)](recipes/seafood-mains/marmitako-basque-tuna-potato-stew.md) — 60 min, 4 servings — ⚠️ incomplete/unverified
- [Mom's Classic Old Bay Crab Cakes](recipes/seafood-mains/old-bay-crab-cakes.md) — 15 min, 4 servings
- [One-Pan Salmon with Creamy Caper Sauce](recipes/seafood-mains/one-pan-salmon-with-creamy-caper-sauce.md) — 15 min, 4 servings
- [Pacotinho de Bacalhau](recipes/seafood-mains/pacotinho-de-bacalhau.md) — 75 min, 4 servings
- [Pan-Seared Lemon Caper Mahi Mahi](recipes/seafood-mains/pan-seared-lemon-caper-mahi-mahi.md) — 85 min, 4 servings
- [Panko-Crusted Baked Salmon](recipes/seafood-mains/panko-crusted-baked-salmon.md) — 20 min, 4 servings
- [Salada de bacalhau com batata e azeitona](recipes/seafood-mains/salada-de-bacalhau-com-batata-e-azeitona.md) — 30 min, 10 servings
- [Salmon Piccata with Spinach](recipes/seafood-mains/salmon-piccata-with-spinach.md) — 20 min, 6 servings
- [Salmon Rockefeller](recipes/seafood-mains/salmon-rockefeller.md) — 30 min, 4 servings
- [Sheet Pan Mediterranean Garlic Butter Baked Salmon](recipes/seafood-mains/sheet-pan-mediterranean-garlic-butter-baked-salmon.md) — 25 min, 6 servings
- [Shrimp Scampi](recipes/seafood-mains/shrimp-scampi.md) — details pending — ⚠️ incomplete/unverified
- [Garlic Steamed Clams](recipes/seafood-mains/garlic-steamed-clams.md) — 20 min, 4 servings

**Sides**
- [Arroz com Lula (Rice with Squid)](recipes/sides/arroz-com-lula.md) — 50 min, 8 servings
- [Easy Red Beans & Rice](recipes/sides/red-beans-rice.md) — 25 min, 6 servings — ⚠️ incomplete/unverified
- [Garlic Herb Sauteed Mushrooms](recipes/sides/garlic-herb-sauteed-mushrooms.md) — 10 min, 4 servings
- [Garlic Parmesan Green Beans: The Side Dish You Didn't Know You Needed!](recipes/sides/garlic-parmesan-green-beans.md) — 15 min, 4 servings
- [Greek Roasted Potatoes Recipe With Lemon & Feta](recipes/sides/greek-roasted-potatoes-with-lemon-feta.md) — 70 min, 14 servings
- [High-Protein Crustless Spinach & Feta Casserole](recipes/sides/crustless-spinach-feta-casserole.md) — "55-60" min, 6 servings
- [Roasted Dill Potatoes](recipes/sides/roasted-dill-potatoes.md) — 50 min, 4 servings — ⚠️ incomplete/unverified
- [The Absolute Best Creamed Spinach Recipe Ever](recipes/sides/best-creamed-spinach.md) — 20 min, 4 servings
- [Turmeric Baked Broccoli](recipes/sides/turmeric-baked-broccoli.md) — 35 min, 4 servings — ⚠️ incomplete/unverified
- [Umami Fried Rice](recipes/sides/umami-fried-rice.md) — 20 min, 8 servings
- [Arroz com Bacalhau do Claude Troisgros](recipes/sides/arroz-com-bacalhau-do-claude-troisgros.md) — 60 min, 8 servings
- [Baked Mushroom Rice](recipes/sides/baked-mushroom-rice.md) — 40 min, 4 servings
- [Baked Parmesan Zucchini Sticks Recipe](recipes/sides/baked-parmesan-zucchini-sticks.md) — 80 min, 40 servings
- [Best Roasted Vegetables](recipes/sides/best-roasted-vegetables.md) — 40 min, 8 servings
- [Buttery Garlicky Cannellini Beans With Feta and Sumac](recipes/sides/buttery-garlicky-cannellini-beans-with-feta-and-sumac.md) — 25 min, 4 servings
- [Cabbage & Potatoes with Bacon](recipes/sides/cabbage-and-potatoes-with-bacon.md) — 25 min, 6 servings
- [Craveable Cauliflower Alfredo Casserole With Peas & Bacon](recipes/sides/cauliflower-alfredo-casserole-with-peas-and-bacon.md) — 40 min, 6 servings
- [Creamy French Onion White Beans](recipes/sides/creamy-french-onion-white-beans.md) — 55 min, 6 servings — ⚠️ incomplete/unverified
- [Creamy High-Protein Cottage Cheese Casserole With Spinach & Feta](recipes/sides/cottage-cheese-casserole-with-spinach-and-feta.md) — 50 min, 6 servings
- [Creamy Poblano Rice Casserole](recipes/sides/creamy-poblano-rice-casserole.md) — 50 min, 12 servings
- [Crispy Parmesan Potatoes](recipes/sides/crispy-parmesan-potatoes.md) — 43 min, 4 servings
- [Decadent Boursin Creamed Spinach With Mushrooms](recipes/sides/boursin-creamed-spinach-with-mushrooms.md) — 15 min, 6 servings
- [Easy Caribbean Rice and Beans](recipes/sides/easy-caribbean-rice-and-beans.md) — 32 min, 8 servings
- [Farofa de Natal](recipes/sides/farofa-de-natal.md) — 30 min, 10 servings
- [Flavorful Cilantro Coconut Rice](recipes/sides/cilantro-coconut-rice.md) — 30 min, 4 servings
- [Golden Red Lentil Dal with Spinach](recipes/sides/golden-red-lentil-dal-with-spinach.md) — 30 min, 4 servings
- [Grandma's Orange Ginger Carrots](recipes/sides/grandmas-orange-ginger-carrots.md) — 20 min, 8 servings — ⚠️ incomplete/unverified
- [High-Protein Mediterranean Spinach Squares](recipes/sides/mediterranean-spinach-squares.md) — 50 min, 9 servings
- [Lemon Basil Rice](recipes/sides/lemon-basil-rice.md) — 25 min, 4 servings
- [Marry Me Chickpeas](recipes/sides/marry-me-chickpeas.md) — 20 min, 6 servings
- [Mediterranean Roasted Greek Potatoes](recipes/sides/roasted-greek-potatoes.md) — 10 servings — ⚠️ incomplete/unverified
- [Mushroom Risotto](recipes/sides/mushroom-risotto.md) — 50 min, 6 servings
- [No-Fuss Refrigerator Bread & Butter Pickles](recipes/sides/refrigerator-bread-and-butter-pickles.md) — 225 min, 20 servings
- [Shiitake and Broccoli in Soy Garlic Sauce](recipes/sides/shiitake-and-broccoli-in-soy-garlic-sauce.md) — 15 min, 3 servings
- [Smashed Potatoes](recipes/sides/smashed-potatoes.md) — 50 min, 4 servings
- [Tasty Turmeric Rice](recipes/sides/turmeric-rice-with-peas-and-lemon.md) — 30 min, 6 servings
- [Lemon Turmeric Broccoli](recipes/sides/lemon-turmeric-broccoli.md) — 10 min, 4 servings
- [Sauteed Spinach & Kale](recipes/sides/sauteed-spinach-and-kale.md) — 20 min, 6 servings

**Soups**
- [Creamy Golden Vegetable Blender Soup](recipes/soups/creamy-golden-vegetable-blender-soup.md) — 45 min, 6 servings
- [Creamy Hungarian Mushroom Soup](recipes/soups/creamy-hungarian-mushroom-soup.md) — 50 min, 6 servings — ⚠️ incomplete/unverified
- [Luxurious Lobster Bisque](recipes/soups/luxurious-lobster-bisque.md) — 80 min, 6 servings — ⚠️ incomplete/unverified
- [Zuppa Toscana (Olive Garden Copycat)](recipes/soups/zuppa-toscana.md) — 45 min, 6 servings
- [Amish Cabbage Soup Recipe With Ground Beef (High Fiber, High Protein)](recipes/soups/amish-cabbage-soup-with-ground-beef.md) — 70 min, 6 servings
- [Brodo di Pollo con Pastina (Italian Chicken Broth with Pastina)](recipes/soups/brodo-di-pollo-con-pastina.md) — 200 min, 6 servings
- [Cajun Potato Soup](recipes/soups/cajun-potato-soup.md) — 50 min, 4-5 servings
- [Caldo de Abóbora com Frango (Pumpkin and Chicken Soup)](recipes/soups/caldo-de-abobora-com-frango.md) — 90 min, 6 servings
- [Chicken and Sausage Gumbo (Classic Dark Roux)](recipes/soups/chicken-and-sausage-gumbo-with-dark-roux.md) — 120 min, 6 servings
- [Colombian Chicken Sancocho](recipes/soups/colombian-chicken-sancocho.md) — 50 min, 6 servings
- [Creamy Spinach and White Bean Soup](recipes/soups/creamy-spinach-and-white-bean-soup.md) — 20 min, 4 servings — ⚠️ incomplete/unverified
- [Easy Aztec Black Bean Soup](recipes/soups/easy-aztec-black-bean-soup.md) — 30 min, 6 servings
- [Easy Chicken & Sausage Gumbo](recipes/soups/chicken-sausage-gumbo.md) — 30 min, 6 servings
- [German Potato Soup with Sausage](recipes/soups/german-potato-soup-with-sausage.md) — 41 min, 8 servings
- [Hearty Lentil Soup with Chorizo and Spinach](recipes/soups/hearty-lentil-soup-with-chorizo-and-spinach.md) — 75 min, "6 to 8" servings — ⚠️ incomplete/unverified
- [High-Protein Creamy Mediterranean White Bean Soup](recipes/soups/creamy-mediterranean-white-bean-soup.md) — 35 min, 6 servings
- [Italian Zuppa di Farro](recipes/soups/italian-zuppa-di-farro.md) — 120 min — ⚠️ incomplete/unverified
- [Kristen Bell's Pickle Soup](recipes/soups/kristen-bells-pickle-soup.md) — details pending — ⚠️ incomplete/unverified
- [Lemon Chicken & Rice Soup](recipes/soups/lemon-chicken-rice-soup.md) — 65 min, 4 servings
- [Mediterranean Vegetable Soup](recipes/soups/mediterranean-vegetable-soup.md) — 35 min, 6 servings
- [Savory Rotisserie Chicken Broth](recipes/soups/savory-rotisserie-chicken-broth.md) — 125 min, 6 servings — ⚠️ incomplete/unverified
- [Smoked Salmon and Leek Soup](recipes/soups/smoked-salmon-and-leek-soup.md) — 30 min, 4 servings
- [Spinach Lentil Soup](recipes/soups/spinach-lentil-soup.md) — 90 min, 6 servings
- [Summer Corn Chowder](recipes/soups/summer-corn-chowder.md) — 90 min, 4 servings
- [The Best Swamp Soup](recipes/soups/swamp-soup.md) — 55 min, 8 servings — ⚠️ incomplete/unverified
- [This Simple Hungarian Goulash Recipe Is So Easy to Make (8 Ingredients)](recipes/soups/hungarian-goulash.md) — 140 min, 8 servings
- [Traditional Colombian Sancocho](recipes/soups/traditional-colombian-sancocho.md) — 120 min — ⚠️ incomplete/unverified
- [Traditional German Potato Soup](recipes/soups/german-potato-soup.md) — 45 min, 4 servings
- [Tuscan White Bean Soup (Minestra di Fagioli)](recipes/soups/tuscan-white-bean-soup.md) — 620 min, 6 servings
- [Ukrainian Mushroom Soup](recipes/soups/ukrainian-mushroom-soup.md) — 40 min, 4 servings — ⚠️ incomplete/unverified


## Flipboard import (in progress)

66 more recipes were added in batch 7 (266 → 332) of converting the ["Food & Flavors" Flipboard magazine](https://flipboard.com/@enetoe/food-flavors-acbn0akgy) (batch 1 added the first 62, batch 2 added 50 more, batch 3 added 56 more, batch 4 added 42 more, batch 5 added 29 more, batch 6 added 11 more — the magazine has about 7,445 saved stories total). Batch 6 had shown a sharp yield drop (11 recipes) because a normal-length scroll kept resurfacing the same ~Dec-2024-and-newer range already covered by batches 1-6. Batch 7 fixed this by scrolling much further in a single session — past 250 real scroll actions, deliberately pushing back to roughly April 2024 story dates, about four months older than any prior batch had reached — which is why yield jumped back up: of 132 raw story URLs collected, 22 were exact-duplicate stories already in the cookbook and 28 were confirmed roundups/listicles, leaving 82 single-recipe candidates; 78 were dispatched to six parallel sub-agents (13 URLs each) after excluding 4 more that were clearly roundups/informational on inspection, and 66 of those 78 were written (12 more were skipped after fetching — 7 turned out to be same-article republishes under a new date path or tip ID not caught by the pre-dispatch exact-URL check, 4 had no actual recipe content (a QVC product ad, a multi-recipe listicle, a comparison article, and a review with no stated quantities), and 1 was a review page that only linked out to the real recipe elsewhere). See `_build/flipboard-batch-7-report.md` for the full accounting (and the batch 1-6 reports for earlier batches), plus `_cookbook-meta-prompt.md` §6c for the duplicate-detection rule this project runs before every batch. Just say "convert the next batch" to continue with batch 8.

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
