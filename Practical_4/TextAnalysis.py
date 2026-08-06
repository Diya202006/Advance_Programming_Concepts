# Simple Text Analysis Tool
 
text = input("Enter a paragraph:\n")
 
text = text.lower()
for ch in ".,!?;:'\"()[]{}":
    text = text.replace(ch, "")
 
words = text.split()
 
total_words = len(words)
 
word_frequency = {}

for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1
 
sorted_words = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)
 
vowels = "aeiou"
vowel_count = 0

for ch in text:
    if ch in vowels:
        vowel_count += 1
 
print("\n--- Text Analysis ---")
print("Total Number of Words:", total_words)

print("\nWord Frequencies:")
for word, count in word_frequency.items():
    print(word, ":", count)

print("\nTop 3 Most Frequent Words:")
for word, count in sorted_words[:3]:
    print(word, ":", count)

print("\nTotal Number of Vowels:", vowel_count)