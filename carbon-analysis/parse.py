from fractions import Fraction
import pandas as pd
import difflib


def parseIngredient(ingredient_line, ingredient):
    ingredient_line = ingredient_line.lower()
    ingredient = ingredient.lower()

    abbr = {"tsp": "teaspoon", "tbsp": "tablespoon", "fl oz": "fluid ounce",
            "c": "cup", "pt": "pint", "qt": "quart", "gal": "gallon"}
    measures = ["tsp", "teaspoon", "tbsp", "tablespoon", "fl oz", "fluid ounce",
                "c", "cup", "pt", "pint", "qt", "quart", "gal", "gallon"]
    grams = {"teaspoon": 5, "tablespoon": 14.8, "fluid ounce": 30,
             "cup": 200, "pint": 450, "quart": 900, "gallon": 3500}

    discretes = {"eggs": 40, "egg": 40, "bananas": 110, "banana": 110}

    for measure in measures:
        if measure in ingredient_line or (measure + "s") in ingredient_line:
            amount = ingredient_line[:ingredient_line.find(measure)]
            if measure in abbr:
                measure = abbr[measure]
            print("measure: " + measure)
            if "/" in amount:
                value = float(sum(Fraction(s) for s in amount.split()))
                return value * grams[measure]
            if "and" in amount:
                value = float(sum(Fraction(s) for s in amount.split(" and ")))
                return value * grams[measure]
            for c in amount:
                if ord(c) == 188:
                    return 1/4 * grams[measure]
                elif ord(c) == 189:
                    return 1/2 * grams[measure]
                elif ord(c) == 190:
                    return 3/4 * grams[measure]
            return int(amount) * grams[measure]

    if not any(char.isdigit() for char in ingredient_line):
        return 0
    # no measure included
    amount = ingredient_line[:ingredient_line.find(ingredient)]
    values = amount.split()
    if ingredient in discretes:
        return discretes[ingredient] * int(values[0])
    return int(values[0])


# data is the rest of the ingreidents such as ["large","eggs"]. it should return the ingredient eggs
# returns none if it doesn't match
def getIngredient(data):
    carbon_data = pd.read_csv("carbon-data.csv")
    items = carbon_data["Item"]


def stupidChar(c):
    if ord(c) == 188:
        return 1/4
    elif ord(c) == 189:
        return 1/2
    elif ord(c) == 190:
        return 3/4
    return -1


def parseIngredient(ingredient_line):
    data = ingredient_line.split()
    # first character is a stupid half thing
    if stupidChar(data[0]) != -1:
        num = stupidChar(data[0])
        del data[0]
    else:
        num = int(data[0])
        if (stupidChar(data[1]) != -1):
            num += stupidChar(data[1])
        del data[0]
        del data[1]

    abbr = {"tsp": "teaspoon", "tbsp": "tablespoon", "fl oz": "fluid ounce",
            "c": "cup", "pt": "pint", "qt": "quart", "gal": "gallon"}
    measures = ["tsp", "teaspoon", "tbsp", "tablespoon", "fl oz", "fluid ounce",
                "c", "cup", "pt", "pint", "qt", "quart", "gal", "gallon"]
    grams = {"teaspoon": 5, "tablespoon": 14.8, "fluid ounce": 30,
             "cup": 200, "pint": 450, "quart": 900, "gallon": 3500}

    discretes = {"eggs": 40, "egg": 40, "bananas": 110, "banana": 110}

    measure = data[0]

    # not a discrete
    if measure in measures:
        if measure in abbr:
            measure = abbr[measure]
        value = num * grams[measure]
        del data[0]
        return (getIngredient(data), value)
    else:  # is a discrete
        item = getIngredient(data)
        value = num * discretes[item]
        return (item, value)


def printLines():
    lines = [
        "2 teaspoons baking soda",
        "2 cups milk",
        "3 1/2 tablespoons sugar",
        "½ teaspoon salt",
        "4 bananas",
        "4 tablespoons oil",
        "2 cups flour",
        "2 eggs"
    ]

    ingredients = [
        "Baking soda",
        "Milk", "Sugar", "Salt", "Bananas", "Oil", "flour", "Eggs"
    ]
    for i in range(len(lines)):
        print(
            f"Ingredient: {ingredients[i]} \nIngredient line: {lines[i]} \ngrams: {parseIngredient(lines[i],ingredients[i])}")


printLines()


def parseIngredientGPT(ingredient_line, ingredient):
    pass
