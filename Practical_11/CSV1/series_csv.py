import pandas as pd
 
data = pd.read_csv("students.csv")
 
marks_series = pd.Series(data["Marks"])

print("CSV Data:")
print(data)

print("\nMarks Series:")
print(marks_series)