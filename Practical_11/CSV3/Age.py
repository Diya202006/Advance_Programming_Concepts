import csv
from datetime import date, datetime
 
with open("birth_info.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["Name"]
        birth_date = datetime.strptime(row["BirthDate"], "%Y-%m-%d").date()
        birth_year = int(row["BirthYear"])
 
today = date.today()
 
age = today.year - birth_date.year
 
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1
 
years_passed = today.year - birth_year
 
print("Name:", name)
print("Birth Date:", birth_date)
print("Birth Year:", birth_year)
print("Current Date:", today)
print("Current Age:", age, "years")
print("Years Passed:", years_passed, "years")