cookbook = {}


def new_recipe(name, ingredients, meal, prep_time):
    cookbook[name] = {
        'ingredients': ingredients,
        'meal': meal,
        'prep_time': prep_time,
    }


def print_all_recipe():
    for key, value in cookbook.items():
        print('')
        print_recipe(key)


def print_recipe(recipe):
    print(f"Recipe for {recipe}:\n"
          f"Ingredients list: {cookbook[recipe]['ingredients']}\n"
          f"To be eaten for {cookbook[recipe]['meal']}.\n"
          f"Takes {cookbook[recipe]['prep_time']} minutes of cooking."
          )


def delete_recipe(recipe):
    del cookbook[recipe]


def usage():
    print(f"Please select an option by typing the corresponding number:\n"
          f"1: Add a recipe\n"
          f"2: Delete a recipe\n"
          f"3: Print a recipe\n"
          f"4: Print the cookbook\n"
          f"5: Quit"
          )


def main():
    cookbook = {}
    options = ['1', '2', '3', '4', '5']
    new_recipe('sandwich', ['ham', 'bread', 'cheese', 'tomatoes'], 'lunch', 10)
    new_recipe('cake', ['flour', 'sugar', 'eggs'], 'dessert', 60)
    ingredients = ['avocado', 'arugula', 'tomatoes', 'spinach']
    new_recipe('salad', ingredients, 'lunch', 15)
    exit = False
    fail1 = 'This option does not exist, please type the corresponding'
    fail2 = 'number.\nTo exit, enter 5.'
    usage()
    while not exit:
        reponse = input('>> ')
        if options.count(reponse) == 0:
            print(fail1, fail2)
            continue
        if reponse == '1':
            name = input("Enter the recipe's name\n>> ")
            ingr_str = input(
                "Enter the recipe's ingredients, separate by /\n>> ")
            ingredients = ingr_str.split('/')
            meal = input("Enter the recipe's type of meal\n>> ")
            prep_time = input(
                "Enter the recipe's preparation time in minutes\n>> ")
            new_recipe(name, ingredients, meal, prep_time)
        elif reponse == '2':
            recipe = input("Enter the deleted recipe\n>> ")
            delete_recipe(recipe)
        elif reponse == '3':
            recipe = input("Enter the printed recipe\n>> ")
            print_recipe(recipe)
        elif reponse == '4':
            print_all_recipe()
        elif reponse == '5':
            exit = True
            print('Cookbook closed.')


if __name__ == '__main__':
    main()
