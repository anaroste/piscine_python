from datetime import datetime
from recipe import Recipe


def get_name(name):
    if type(name) != str:
        print('name is not a string')
        exit()
    return name


class Book:
    def __init__(self, name):
        self.name = name
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = {
            'starter': [],
            'lunch': [],
            'dessert': [],
        }

    def get_recipe_by_name(self, name):
        for elt in self.recipes_list['starter']:
            if elt.name == name:
                print(elt)
                return elt
        for elt in self.recipes_list['lunch']:
            if elt.name == name:
                print(elt)
                return elt
        for elt in self.recipes_list['dessert']:
            if elt.name == name:
                print(elt)
                return elt
        print('This recipe is not in this book')
        exit()

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        for elt in self.recipes_list[recipe_type]:
            print(elt)
        return self.recipes_list[recipe_type]

    def add_recipe(self, recipe):
        if type(recipe) != Recipe:
            print('Recipe is not Recipe type')
            exit()
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()

    def __str__(self):
        return f"{self.name}, last update : {self.last_update}"
