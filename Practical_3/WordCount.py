# Program to count the total number of words in a sentence

sentence = input("Enter a sentence: ")

count = 0
in_word = False

for ch in sentence:
    if ch != ' ':
        if in_word == False:
            count += 1
            in_word = True
    else:
        in_word = False

print("Total number of words =", count)