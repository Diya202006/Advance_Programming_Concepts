# Program to Check Anagrams
 
def normalize(text):
    text = text.lower()
    result = ""

    for ch in text:
        if ch.isalnum():       
            result += ch

    return result
 
def is_anagram(str1, str2):
    str1 = normalize(str1)
    str2 = normalize(str2)
 
    freq1 = {}
    freq2 = {}

    for ch in str1:
        if ch in freq1:
            freq1[ch] += 1
        else:
            freq1[ch] = 1

    for ch in str2:
        if ch in freq2:
            freq2[ch] += 1
        else:
            freq2[ch] = 1

    return freq1 == freq2
 
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if is_anagram(string1, string2):
    print("The strings are Anagrams.")
else:
    print("The strings are Not Anagrams.")