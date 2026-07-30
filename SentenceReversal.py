# Program to reverse the order of words in a sentence

sentence = input("Enter a sentence: ")

words = sentence.split()

for i in range(len(words) - 1, -1, -1):
    print(words[i], end=" ")