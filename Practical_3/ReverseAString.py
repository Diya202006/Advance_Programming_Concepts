# Program to reverse a string without using built-in functions

string = input("Enter a string: ")

reverse = ""

for i in string:
    reverse = i + reverse 

print("Reversed string:", reverse)