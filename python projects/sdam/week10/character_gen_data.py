import json
import pandas as pd

file = open("char_classes.json")
data = json.load(file)

table = pd.DataFrame.from_dict(data, orient="index")

table.columns = ["Strength", "Intelligence", "Wisdom", "Dexterity", "Constitution"]

print(table)