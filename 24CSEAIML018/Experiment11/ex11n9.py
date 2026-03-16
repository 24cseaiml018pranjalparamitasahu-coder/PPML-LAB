import pandas as pd
data={
    'Math':[90,85,80,95],
    'Science':[88,82,85,90],
    'English':[78,75,80,85]
}
df=pd.DataFrame(data)
print("Dataframe:",df)
corelation=df.corr()
print("\n Correlation matrix:",corelation)