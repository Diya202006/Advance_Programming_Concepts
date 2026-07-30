# Program to count the occurrences of a word in a sentence

sentence = input("Enter a sentence: ")
search = input("Enter the word to search: ")

word = ""
count = 0

for ch in sentence + " ":
    if ch != ' ':
        word += ch
    else:
        if word == search:
            count += 1
        word = ""

print("Occurrences of", search, "=", count)