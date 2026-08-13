# Program to demonstrate read(), readline() and readlines()
 
file = open("student.txt", "w")

file.write("Name: Diya\n")
file.write("Branch: CSE\n")
file.write("Year: Third Year\n")
file.write("College: Engineering College\n")

file.close()
 
file = open("student.txt", "r")

data = file.read()

print("----- Using read() -----")
print(data)

file.close()

file = open("student.txt", "r")

print("----- Using readline() -----")

line1 = file.readline()
line2 = file.readline()
line3 = file.readline()

print(line1, end="")
print(line2, end="")
print(line3, end="")

file.close() 

file = open("student.txt", "r")

lines = file.readlines()

print("\n----- Using readlines() -----")

for line in lines:
    print(line, end="")

file.close()