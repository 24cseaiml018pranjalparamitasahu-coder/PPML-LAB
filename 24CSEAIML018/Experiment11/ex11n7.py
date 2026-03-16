import pandas as pd
data={
    'Name':['Alice','Bob','Charlie'],
    'Age':[25,30,35],
    'City':['NewYork','San Fransisco','Los Angeles']
}
df=pd.DataFrame(data)
print("Dataframe:",df)
print("\n Age column:",df['Age'])
print("\n Row at index 1:",df.iloc[1])