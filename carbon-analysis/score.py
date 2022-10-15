import pandas as pd
#from parse import parseIngredient
import difflib

# https://www.geeksforgeeks.org/how-to-do-fuzzy-matching-on-pandas-dataframe-column-using-python/
carbon_data = pd.read_csv("carbon-data.csv")
items = carbon_data['Item']
print(list(items))
# print(carbon_data.head())
# print(carbon_data.loc[carbon_data['Item'] == 'BEER IN CAN'])

difflib.get_close_matches(
    "egg", ["eggs", "milk", "carrots", "celery", "steak"])


def getScore(ingredient_lines, servings):
    """
    ingredients is a string highlighted by the user, containing ingredients and amounts
    servings is the number of servings (int)
    """
    # creating a data frame
    carbon_data = pd.read_csv("carbon-data.csv")
    print(carbon_data.head())

    parsed_ingredients = []
   # for idx, line in enumerate(ingredient_lines):
    #parsed_ingredients.append(parseIngredient(line, ingredients[idx]))
