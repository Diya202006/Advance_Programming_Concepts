# Writing data into a file

file = open("student.txt", "w")

file.write("Name: Diya\n")
file.write("Branch: Computer Science\n")
file.write("Year: Third Year\n")

file.close()


# Reading data from the file

file = open("student.txt", "r")

data = file.read()

print(data)

file.close()