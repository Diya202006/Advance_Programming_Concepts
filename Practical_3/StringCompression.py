# Program for String Compression

string = input("Enter a string: ")

compressed = ""
count = 1

for i in range(len(string)):
    if i == len(string) - 1:
        compressed += string[i] + str(count)
    elif string[i] == string[i + 1]:
        count += 1
    else:
        compressed += string[i] + str(count)
        count = 1

if len(compressed) < len(string):
    print("Compressed string:", compressed)
else:
    print("Original string:", string)