import pandas as pd 
data = {
    "namew": ["Adarsh", "Rohit", "Saurabh", "Ramesh"],
    "age": [25, 30, 22, 28],
    "city": ["Delhi", "Mumbai", "Bangalore", "Chennai"]
}
df = pd.DataFrame(data)
print(df)
df.to_csv("output.csv", index=False)
