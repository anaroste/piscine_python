from recipe import Recipe
from book import Book

pain = Recipe('pain', 3, 60, ['farine', 'eau', 'levain'], 'lunch',
              'Accompagne un plat')

nutela = Recipe('nutela', 1, 1, ['noisette', 'huile de palme'], 'starter',
                'A mettre sur une tartine')
confiture = Recipe('confiture', 1, 1, ['fruit', 'sucre'], 'starter',
                'A mettre sur une tartine de pain')

new_book = Book('cuisine A a Z')
new_book.add_recipe(pain)
new_book.add_recipe(nutela)
new_book.add_recipe(confiture)
if pain == new_book.get_recipe_by_name('pain'):
    print ('Le pain est bon')
new_book.get_recipes_by_types('starter')
