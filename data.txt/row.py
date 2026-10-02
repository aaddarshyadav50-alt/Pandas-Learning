import pandas as pd
df=pd.read_json(r"C:\Users\Adarsh Yadav\Downloads\sample_Data.json")
print(df)
print ('display first 5 rows of the dataframe')
print(df.head())
print ('display last 5 rows of the dataframe')
print(df.tail())