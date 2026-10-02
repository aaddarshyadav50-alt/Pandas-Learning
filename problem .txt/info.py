import pandas as pd
df=pd.read_json(r"C:\Users\Adarsh Yadav\Downloads\sample_Data.json")
print('displaying the info from json')
print(df.info())