# Read a text file and find the longest word present in the file. 
 
file = open("student.txt", "r")
 
content = file.read()
 
words = content.split()
 
longest_word = max(words, key=len)
 
print("Longest word:", longest_word)
 
file.close()