import pandas as pd
 
df = pd.read_csv("students.csv")
 
print("Student DataFrame:")
print(df)
 
print("\nFirst 2 rows:")
print(df.head(2))
 
print("\nColumn Names:")
print(df.columns)
 
print("\nDataFrame Information:")
print(df.info())