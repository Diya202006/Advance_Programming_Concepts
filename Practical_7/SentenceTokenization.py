import nltk
from nltk.tokenize import sent_tokenize

text = "Hello, I am learning Natural Language Processing. NLTK is a Python library. It is useful for NLP."

sentences = sent_tokenize(text)

print("Original Text:")
print(text)

print("\nSentence Tokens:")

for sentence in sentences:
    print(sentence)