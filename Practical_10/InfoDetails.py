#  Read a text file and calculate the number of alphabets, digits, spaces, and special characters. 
 
file = open("student.txt", "r")
 
content = file.read()
 
alphabets = 0
digits = 0
spaces = 0
special = 0
 
for char in content:
    if char.isalpha():
        alphabets = alphabets + 1
    elif char.isdigit():
        digits = digits + 1
    elif char == " ":
        spaces = spaces + 1
    else:
        special = special + 1
 
print("Total alphabets:", alphabets)
print("Total digits:", digits)
print("Total spaces:", spaces)
print("Total special characters:", special)
 
file.close()