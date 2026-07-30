# Program to convert the first letter of every word to uppercase

sentence = input("Enter a sentence: ")

result = ""
new_word = True

for ch in sentence:
    if new_word and 'a' <= ch <= 'z':
        result += chr(ord(ch) - 32)  
        new_word = False
    else:
        result += ch
        if ch == ' ':
            new_word = True
        else:
            new_word = False

print("Title Case:", result)