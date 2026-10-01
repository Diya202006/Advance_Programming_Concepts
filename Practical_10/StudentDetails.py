# Create and write Student data into student.txt

file = open("student.txt", "w")

file.write("Name: Diya Khamkar\n")
file.write("Roll Number: 101\n")
file.write("Branch: Computer Science and Engineering\n")
file.write("Semester: 5\n")

file.close()

print("Student details written successfully to student.txt") 