# Program to replace all occurrences of a character

string = input("Enter a string: ")
old_char = input("Enter the character to replace: ")
new_char = input("Enter the new character: ")

result = ""

for ch in string:
    if ch == old_char:
        result += new_char
    else:
        result += ch

print("Updated string:", result)