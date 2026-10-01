#  Read a text file and count the number of vowels and consonants present in the file. 
 
file = open("student.txt", "r")
 
content = file.read()
 
vowels = 0
consonants = 0
 
for char in content:
    if char.isalpha():
        if char.lower() in "aeiou":
            vowels = vowels + 1
        else:
            consonants = consonants + 1
 
print("Total number of vowels:", vowels)
print("Total number of consonants:", consonants)
 
file.close()