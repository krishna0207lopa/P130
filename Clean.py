import pandas as pd
import csv 

df = pd.read_csv("Stars_data.csv")

del df["Luminosity"]

df = df.rename({
    "Star_name": "Star_name",
    "Distance":"distance_from_star",
    "Mass" : "Mass_of_star",
    "Radius":"Radius_of_star",
},
axis="columns")
print(df.shape)
print(list(df))
df.to_csv("stars.csv")