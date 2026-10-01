# Write a program to count the total number of characters in a text file, including spaces. 

file = open("student.txt", "r")
 
content = file.read()
 
count = len(content)
 
print("Total number of characters:", count)
 
file.close()