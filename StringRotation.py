# Program to check whether one string is a rotation of another

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if len(string1) != len(string2):
    print("No")
else:
    temp = string1 + string1

    found = False

    for i in range(len(temp) - len(string2) + 1):
        match = True

        for j in range(len(string2)):
            if temp[i + j] != string2[j]:
                match = False
                break

        if match:
            found = True
            break

    if found:
        print("Yes")
    else:
        print("No")