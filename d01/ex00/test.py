from recipe import Recipe
from book import Book

# The next line should print an error
# invalid_parameter = Recipe(42, "42", 49, None, None)

pain = Recipe('pain', 3, 60, ['farine', 'eau', 'levain'], 'lunch',
              'Accompagne un plat')
nutela = Recipe('nutela', 1, 1, ['noisette', 'huile de palme'], 'starter',
                'A mettre sur une tartine')
confiture = Recipe('confiture', 1, 1, ['fruit', 'sucre'], 'starter',
                'A mettre sur une tartine de pain')

# Invalid creation of Book
# invalid_book = Book(0)

new_book = Book('cuisine A a Z')
print(f"Creation date : {new_book.creation_date}\n"
      f"Last_update : {new_book.last_update}\n\n")

new_book.add_recipe(pain)
new_book.add_recipe(nutela)
new_book.add_recipe(confiture)

if pain == new_book.get_recipe_by_name('pain'):
    print ('Le retour de get_recipe_by_name est bon\n\n')

# new_book.get_recipe_by_name('NonExisting')

print(f"Should print 'nutela' and 'confiture' not 'pain'")
new_book.get_recipes_by_types('starter')

print(f"\n\n{new_book.last_update}")
print(f"Should print anything")
new_book.get_recipes_by_types('dessert')
print(f"{new_book.last_update}\n\n")

new_book.get_recipes_by_types('NonExisting')