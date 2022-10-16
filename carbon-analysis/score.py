import pandas as pd
#from parseHTML import parse
import difflib
from fractions import Fraction


# https://www.geeksforgeeks.org/how-to-do-fuzzy-matching-on-pandas-dataframe-column-using-python/
carbon_data = pd.read_csv("data/carbon-data.csv")
items = carbon_data['Item']
carbonItems = [x.lower() for x in items]

water_data = pd.read_csv("data/water-data.csv")
water_items = water_data['Item']
waterItems = [x.lower() for x in water_items]

# print(carbon_data.head())
# print(carbon_data.loc[carbon_data['Item'] == 'BEER IN CAN'])


def getIngredient(ingr):
    choices = difflib.get_close_matches(ingr, items)
    if choices == []:
        return "none"
    return choices[0]


def getScores(ingredients, servings):
    grams = {"teaspoon": 5, "tablespoon": 14.8, "fluid ounce": 30,
             "cup": 200, "pint": 450, "quart": 900, "gallon": 3500, "pound": 450}

    ingr_scores = {}
    for (amt, unit, i) in ingredients:
        ingr = getIngredient(i.split(" ")[-1].lower())
        if "/" in amt:
            amt += float(Fraction(amt))
        else:
            amt = float(amt)
        unit = unit.lower()
        if ingr == "none":
            continue
        if unit not in ["g", "gram", "grams"]:
            if unit[-1] == 's':
                unit = unit[:-1]
            if unit in grams:
                amt *= grams[unit]
            else:
                continue

        waterScore = getWaterScore(ingr, amt)/servings
        carbonScore = getCarbonScore(ingr, amt)/servings
        ingr_scores[ingr] = {
            "carbonScore": carbonScore, "waterScore": waterScore}

    scores = [val for val in ingr_scores.values()]
    totalCarbonScore = sum([dict["carbonScore"] for dict in scores])/servings
    totalWaterScore = sum([dict["waterScore"] for dict in scores])/servings

    return (ingr_scores, totalCarbonScore, totalWaterScore)


def getWaterScore(ingr, grams):
    """
    ingredients is a string highlighted by the user, containing ingredients and amounts
    servings is the number of servings (int)
    returns a list of [litres of water/ kg food] per serving, for each ingredient
    """
    kg = grams * 1000
    data = carbonItems.loc[carbonItems['Item'] == ingr]
    carbon = data['water'][0]
    return carbon * kg


def getCarbonScore(ingr, grams):
    """
    ingredients is a string highlighted by the user, containing ingredients and amounts
    servings is the number of servings (int)
    returns a list of [kg CO2 eq/ kg food] per serving, for each ingredient
    """
    kg = grams * 1000
    data = carbonItems.loc[carbonItems['Item'] == ingr]
    carbon = data['carbon'][0]
    return carbon * kg
