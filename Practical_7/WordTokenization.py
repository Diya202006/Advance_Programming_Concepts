import nltk
from nltk.tokenize import word_tokenize

text = "Hello, I am learning Natural Language Processing."

words = word_tokenize(text)

print("Original Text:")
print(text)

print("\nWord Tokens:")
print(words)