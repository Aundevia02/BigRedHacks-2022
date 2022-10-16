import pandas as pd
import difflib
from fractions import Fraction


carbon_data = pd.read_csv("data/carbon-data.csv")
items = carbon_data['Item']
carbonItems = [x.lower().strip() for x in items]

water_data = pd.read_csv("data/water-data.csv")
water_items = water_data['Item']
waterItems = [x.lower().strip() for x in water_items]


def getIngredient(ingr):
    choices = difflib.get_close_matches(ingr, carbonItems, cutoff=0.8)
    if choices == []:
        return "none"

    return choices[0]


def getIngredientWater(ingr):
    ingr = ingr.lower()
    choices = difflib.get_close_matches(ingr, waterItems, cutoff=0.8)
    if choices == []:
        return "none"
    #print(f"ingr: {ingr}, choice: {choices[0]}")
    return choices[0]


def stupidChar(c):
    if ord(c) == 188:
        return 1/4
    elif ord(c) == 189:
        return 1/2
    elif ord(c) == 190:
        return 3/4
    return -1


def parseAmount(amt):
    if stupidChar(amt[0]) != -1:
        return stupidChar(amt[0])
    else:
        num = float(amt[0])
        return num


def getScores(ingredients, servings):
    grams = {"teaspoon": 5, "tablespoon": 14.8, "fluid ounce": 30,
             "cup": 200, "pint": 450, "quart": 900, "gallon": 3500, "pound": 450}

    ingr_scores = {}
    for (amt, unit, i) in ingredients:
        i = i.strip().replace(",", "").replace(".", "")
        #print(f"amt: {amt}, unit: {unit}, ingr: {i}")

        ingr = getIngredient(i.split(" ")[-1].lower())
        amt = parseAmount(amt)
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

        waterScore = round(getWaterScore(ingr, amt), 4)
        carbonScore = round(getCarbonScore(ingr, amt), 4)
        ingr_scores[ingr] = {
            "carbonScore": carbonScore, "waterScore": waterScore}

    scores = [val for val in ingr_scores.values()]
    totalCarbonScore = round(sum([dict["carbonScore"] for dict in scores]), 4)
    totalWaterScore = round(sum([dict["waterScore"] for dict in scores]), 4)

    return (ingr_scores, totalCarbonScore, totalWaterScore)


def getWaterScore(ingr, grams):
    """
    ingredients is a string highlighted by the user, containing ingredients and amounts
    servings is the number of servings (int)
    returns a list of [litres of water/ kg food] per serving, for each ingredient
    """
    kg = grams/1000
    ingr = getIngredientWater(ingr).upper()
    data = water_data.loc[water_data['Item'] == ingr]
    if len(list(data['Water'])) == 0:
        return 0
    water = list(data['Water'])[0]
    return water * kg


def getCarbonScore(ingr, grams):
    """
    ingredients is a string highlighted by the user, containing ingredients and amounts
    servings is the number of servings (int)
    returns a list of [kg CO2 eq/ kg food] per serving, for each ingredient
    """
    kg = grams/1000
    ingr = ingr.upper()
    data = carbon_data.loc[carbon_data['Item'] == ingr]
    carbon = list(data['Carbon'])[0]
    return carbon * kg
