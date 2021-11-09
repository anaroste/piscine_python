def get_name(name):
    if type(name) != str:
        print('name is not a string')
        exit()
    return name


def get_cooking_lvl(cooking_lvl):
    if type(cooking_lvl) != int:
        print('cooking_lvl is not int type')
        exit()
    if 1 < cooking_lvl > 5:
        print('cooking_lvl is not between 1 and 5')
        exit()
    return cooking_lvl


def get_cooking_time(cooking_time):
    if type(cooking_time) != int:
        print('cooking_time is not int type')
        exit()
    if 0 > cooking_time:
        print('cooking_time is negative')
        exit()
    return cooking_time


def get_ingredients(ingredients):
    if type(ingredients) != list:
        print('ingredients is not list type')
        exit()
    for elt in ingredients:
        if type(elt) != str:
            print('An ingredient is not a string')
            exit()
    return ingredients


def get_description(description):
    if type(description) != str:
        print('description is not a string')
        exit()
    return description


def get_recipe_type(recipe_type):
    if type(recipe_type) != str:
        print('recipe_type is not a string')
        exit()
    if recipe_type != 'starter' and recipe_type != 'lunch' and \
       recipe_type != 'dessert':
        print('recipe_type is an unknown value')
        exit()
    return recipe_type


class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients,
                 recipe_type, description=""):
        self.name = get_name(name)
        self.cooking_lvl = get_cooking_lvl(cooking_lvl)
        self.cooking_time = get_cooking_time(cooking_time)
        self.ingredients = get_ingredients(ingredients)
        self.description = get_description(description)
        self.recipe_type = get_recipe_type(recipe_type)

    def __str__(self):
        ret = (f"{self.name}:\n"
               f"Ingredients list: {self.ingredients}\n"
               f"To be eaten for {self.recipe_type}.\n"
               f"Takes {self.cooking_time} minutes of cooking.\n"
               f"Difficult : {self.cooking_lvl} / 5.\n"
               f"{self.description}"
               )
        return ret
