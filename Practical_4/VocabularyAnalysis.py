# Vocabulary Analysis of Two Books
 
book1 = input("Enter the text of Book 1:\n").lower()
 
book2 = input("\nEnter the text of Book 2:\n").lower()
 
for ch in ".,!?;:'\"()[]{}":
    book1 = book1.replace(ch, "")
    book2 = book2.replace(ch, "")
 
words_book1 = set(book1.split())
words_book2 = set(book2.split())
 
common_words = words_book1.intersection(words_book2)
unique_book1 = words_book1.difference(words_book2)
unique_book2 = words_book2.difference(words_book1)
all_unique_words = words_book1.union(words_book2)
 
print("\n--- Vocabulary Analysis ---")
print("Unique words in Book 1:", words_book1)
print("Unique words in Book 2:", words_book2)

print("\nCommon words:", common_words)

print("\nWords unique to Book 1:", unique_book1)
print("Words unique to Book 2:", unique_book2)

print("\nTotal unique words across both books:", len(all_unique_words))
print("All unique words:", all_unique_words)
