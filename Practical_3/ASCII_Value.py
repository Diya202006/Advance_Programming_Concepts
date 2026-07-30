# Program to display each character and its ASCII value

string = input("Enter a string: ")

for ch in string:
    print(ch, "=", ord(ch))