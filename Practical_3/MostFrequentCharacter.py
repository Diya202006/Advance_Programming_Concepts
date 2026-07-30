# Program to find the most frequent character in a string

string = input("Enter a string: ")

max_count = 0
max_char = ""

checked = ""

for i in range(len(string)):
    if string[i] not in checked:
        count = 0

        for j in range(len(string)):
            if string[i] == string[j]:
                count += 1

        if count > max_count:
            max_count = count
            max_char = string[i]

        checked += string[i]

print("Most frequent character:", max_char)
print("Frequency:", max_count)