# Program to find the second most frequent character

string = input("Enter a string: ")

first_char = ""
second_char = ""
first_count = 0
second_count = 0

checked = ""

for i in range(len(string)):
    if string[i] not in checked:
        count = 0

        for j in range(len(string)):
            if string[i] == string[j]:
                count += 1

        if count > first_count:
            second_count = first_count
            second_char = first_char

            first_count = count
            first_char = string[i]

        elif count > second_count and count != first_count:
            second_count = count
            second_char = string[i]

        checked += string[i]

print("Second most frequent character:", second_char)
print("Frequency:", second_count)