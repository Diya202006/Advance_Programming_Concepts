# Character Frequency Counter
 
text = input("Enter a string: ")
 
choice = input("Ignore case? (yes/no): ")

if choice.lower() == "yes":
    text = text.lower()
 
frequency = {}
 
for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1
 
sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
 
print("\n--- Character Frequency ---")
for ch, count in sorted_frequency:
    if ch == " ":
        print("'Space' :", count)
    else:
        print(ch, ":", count)