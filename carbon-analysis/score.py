import pandas as pd
from parseHTML import parse
import difflib

# https://www.geeksforgeeks.org/how-to-do-fuzzy-matching-on-pandas-dataframe-column-using-python/
carbon_data = pd.read_csv("data/carbon-data.csv")
items = carbon_data['Item']
print(list(items))
# print(carbon_data.head())
# print(carbon_data.loc[carbon_data['Item'] == 'BEER IN CAN'])


def getScores(ingredient_string, servings):
    pass


def getWaterScores(ingredients, servings):
    """
    ingredients is a string highlighted by the user, containing ingredients and amounts
    servings is the number of servings (int)
    returns a list of [litres of water/ kg food] per serving, for each ingredient
    """

    water_data = pd.read_csv("water-data.csv")
    print(water_data.head())


def getCarbonScores(ingredients, servings):
    """
    ingredients is a string highlighted by the user, containing ingredients and amounts
    servings is the number of servings (int)
    returns a list of [kg CO2 eq/ kg food] per serving, for each ingredient
    """
    # creating a data frame
    carbon_data = pd.read_csv("carbon-data.csv")
    print(carbon_data.head())

    parsed_ingredients = []
    for idx, line in enumerate(ingredientLines):
        parsed_ingredients.append(parseIngredient(line, ingredients[idx]))


def find_ingredient(string, all_ingredients):
    pass
