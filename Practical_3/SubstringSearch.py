# Program to check whether a substring exists in a string

string = input("Enter the main string: ")
substring = input("Enter the substring: ")

found = False

for i in range(len(string) - len(substring) + 1):
    match = True

    for j in range(len(substring)):
        if string[i + j] != substring[j]:
            match = False
            break

    if match:
        found = True
        break

if found:
    print("Substring found.")
else:
    print("Substring not found.")