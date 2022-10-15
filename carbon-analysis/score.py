import pandas as pd
from parse import parseIngredient
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# https://www.geeksforgeeks.org/how-to-do-fuzzy-matching-on-pandas-dataframe-column-using-python/


def matchNames(to_match, data):
    data_list = data['Item'].tolist()

    mat1 = []
    mat2 = []
    p = []

    # printing the pandas dataframes
    print("First dataframe:\n", dframe1,
          "\nSecond dataframe:\n", dframe2)

    # converting dataframe column to list
    # of elements
    # to do fuzzy matching
    list1 = dframe1['name'].tolist()
    list2 = dframe2['name'].tolist()

    # taking the threshold as 82
    threshold = 82

    # iterating through list1 to extract
    # it's closest match from list2
    for i in list1:
        mat1.append(process.extract(i, list2, limit=2))
    dframe1['matches'] = mat1

    # iterating through the closest matches
    # to filter out the maximum closest match
    for j in dframe1['matches']:
        for k in j:
            if k[1] >= threshold:
                p.append(k[0])
        mat2.append(",".join(p))
        p = []

    # storing the resultant matches back to dframe1
    dframe1['matches'] = mat2
    print("\nDataFrame after Fuzzy matching:")
    dframe1

    threshold = 82
    print(data_list)


carbon_data = pd.read_csv("carbon-data.csv")
print(carbon_data.head())


def getScore(ingredientLines, ingredients):
    # creating a data frame
    carbon_data = pd.read_csv("carbon-data.csv")
    print(df.head())

    parsed_ingredients = []
    # for idx, line in enumerate(ingredientLines):
    #     parsed_ingredients.append(parseIngredient(line, ingredients[idx]))
