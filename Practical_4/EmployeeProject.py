# Employee Project Management using Sets
 
project1 = set(input("Enter employee names for Project 1 (separated by spaces): ").split())
 
project2 = set(input("Enter employee names for Project 2 (separated by spaces): ").split())
 
common_employees = project1.intersection(project2)
 
only_project1 = project1.difference(project2)
 
only_project2 = project2.difference(project1)
 
all_employees = project1.union(project2)
 
print("\n--- Employee Analysis ---")
print("Employees working on both projects:", common_employees)
print("Employees working only on Project 1:", only_project1)
print("Employees working only on Project 2:", only_project2)
print("Total unique employees:", all_employees)