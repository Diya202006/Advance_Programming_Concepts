# Program to check whether two strings are anagrams

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

if len(string1) != len(string2):
    print("The strings are not Anagrams.")
else:
    matched = True

    for ch in string1:
        count1 = 0
        count2 = 0

        for c in string1:
            if c == ch:
                count1 += 1

        for c in string2:
            if c == ch:
                count2 += 1

        if count1 != count2:
            matched = False
            break

    if matched:
        print("The strings are Anagrams.")
    else:
        print("The strings are not Anagrams.")