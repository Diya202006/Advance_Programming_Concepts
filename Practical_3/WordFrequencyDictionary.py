# Program to count the frequency of every word in a paragraph

paragraph = input("Enter a paragraph: ")

words = paragraph.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word Frequencies:")

for word in frequency:
    print(word, "=", frequency[word])