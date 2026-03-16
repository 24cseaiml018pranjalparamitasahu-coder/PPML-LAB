import pandas as pd
df_csv=pd.read_csv("sample.csv")
print("Dataframe from csv:",df_csv)
df_json=pd.read_json("sample.json")
print("Dataframe from json:",df_json)