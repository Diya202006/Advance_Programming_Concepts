# Write a program to count and display the total number of lines present in a text file.

file = open("student.txt", "r")
 
count = 0

for line in file:
    count = count + 1
 
print("Total number of lines:", count)
 
file.close()