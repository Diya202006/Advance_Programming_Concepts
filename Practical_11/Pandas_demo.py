import pandas as pd

data = {
    "Name": ["Amit", "Rahul", "Priya"],
    "Age": [20, 21, 20],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)