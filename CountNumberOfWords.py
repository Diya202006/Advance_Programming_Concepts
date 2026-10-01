# Write a program to count the total number of words present in a text file. 
 
file = open("student.txt", "r")
 
content = file.read()
 
words = content.split()
 
count = len(words)
 
print("Total number of words:", count)
 
file.close()