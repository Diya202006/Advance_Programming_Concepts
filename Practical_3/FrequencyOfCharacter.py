# Program to find the frequency of a character in a string

string = input("Enter a string: ")
char = input("Enter the character to find: ")

count = 0

for ch in string:
    if ch == char:
        count += 1

print("Frequency of ", char, "=", count)
