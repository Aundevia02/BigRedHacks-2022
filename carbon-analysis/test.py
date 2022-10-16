import pandas as pd
import difflib

carbon_data = pd.read_csv("data/carbon-data.csv")
items = carbon_data['Item']
items = [x.lower() for x in items]

print(difflib.get_close_matches("milk", items, cutoff=.8))
