# Program to display the frequency of every character in a string

string = input("Enter a string: ")

printed = ""

for i in range(len(string)):
    if string[i] not in printed:
        count = 0

        for j in range(len(string)):
            if string[i] == string[j]:
                count += 1

        print(string[i], "=", count)
        printed += string[i]