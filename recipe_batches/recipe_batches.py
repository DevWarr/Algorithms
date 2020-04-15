#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):

    # Loop through the recipe keys
    first_loop = True
    max_batches = 0
    for i in recipe:
        # The ingredients we have,
        #     divided by the amount the recipe needs
        #     should give us the number of whole batches
        # If we don't have the ingredients in our ingredients, return 0

        if first_loop == True:
            # If it's the first loop, set the max_batches immediately.
            count = ingredients.get(i, 0)
            if count == 0:
                return 0
            max_batches = count // recipe[i]
            first_loop = False

        else:
            # Otherwise, loop through the whole array,
            #     and the lowest number from the above division is
            #     the number of whole batches we can make
            count = ingredients[.get(i, 0)]
            if count == 0:
                return 0
            if count // recipe[i] < max_batches:
                max_batches = count // recipe[i]
    return max_batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
