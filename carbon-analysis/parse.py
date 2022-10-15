import re
from fractions import Fraction


def parseIngredient(ingredient_line, ingredient):
    ingredient_line = ingredient_line.lower()
    ingredient = ingredient.lower()

    abbr = {"tsp": "teaspoon", "tbsp": "tablespoon", "fl oz": "fluid ounce",
            "c": "cup", "pt": "pint", "qt": "quart", "gal": "gallon"}
    measures = ["tsp", "teaspoon", "tbsp", "tablespoon", "fl oz", "fluid ounce",
                "c", "cup", "pt", "pint", "qt", "quart", "gal", "gallon"]
    grams = {"teaspoon": 5, "tablespoon": 14.8, "fluid ounce": 30,
             "cup": 200, "pint": 450, "quart": 900, "gallon": 3500}

    for measure in measures:
        if measure in ingredient_line or (measure + "s") in ingredient_line:
            amount = ingredient_line[:ingredient_line.find(measure)]
            if measure in abbr:
                measure = abbr[measure]
            print("measure: " + measure)
            if "/" in amount:
                value = float(sum(Fraction(s) for s in amount.split()))
                return value
            if "and" in amount:
                value = float(sum(Fraction(s) for s in amount.split(" and ")))
                return value
            for c in amount:
                if ord(c) == 188:
                    return 1/4
                elif ord(c) == 189:
                    return 1/2
                elif ord(c) == 190:
                    return 3/4
            return amount

    if not any(char.isdigit() for char in ingredient_line):
        return 0
    # no measure included
    amount = ingredient_line[:ingredient_line.find(ingredient)]
    values = amount.split()
    return int(values[0])


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


def parseIngredientGPT(ingredient_line, ingredient):
    pass
