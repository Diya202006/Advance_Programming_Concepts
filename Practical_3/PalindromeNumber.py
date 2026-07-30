# Program to check whether a string is a palindrome

string = input("Enter a string: ")

reverse = ""

for i in string:
    reverse = i + reverse

if string == reverse:
    print("The string is a Palindrome.")
else:
    print("The string is Not a Palindrome.")