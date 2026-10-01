# Write a program to append additional student information to an existing file without deleting its previous contents. 

file = open("student.txt", "a")
 
file.write("\nAddress: Kolhapur\n")
file.write("Email: diya@example.com\n")
file.write("Phone: 9876543210\n")
 
file.close()

print("Additional student information added successfully.")