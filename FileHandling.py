# File Handling in Python
# Modes: r, w, a, r+, w+, a+, rb, wb, ab
 
file = open("sample.txt", "w")
file.write("Hello Python\n")
file.write("Python Programming.....!\n")
file.close()

print("1. w mode: Data written successfully.")
 
file = open("sample.txt", "r")
data = file.read()
file.close()

print("\n2. r mode: Reading file")
print(data)
 
file = open("sample.txt", "a")
file.write("Hello Everyone....!\n")
file.close()

print("3. a mode: Data appended successfully.")

file = open("sample.txt", "r+")
data = file.read()

print("\n4. r+ mode: Reading and writing")
print(data)

file.write("Good Morning.....\n")
file.close()

file = open("write_read.txt", "w+")

file.write("Have a nice Day.....\n")
 
file.seek(0)

data = file.read()
file.close()

print("\n5. w+ mode:")
print(data)
 
file = open("append_read.txt", "a+")

file.write("Best Luck for your Future....\n")

file.seek(0)

data = file.read()
file.close()

print("\n6. a+ mode:")
print(data)
 
file = open("binary.txt", "wb")

data = b"Hello Python Binary File"
file.write(data)

file.close()

print("7. wb mode: Binary data written successfully.")
 
file = open("binary.txt", "rb")

data = file.read()
file.close()

print("\n8. rb mode:")
print(data)
 
file = open("binary.txt", "ab")

data = b"\nAdditional binary data"
file.write(data)

file.close()

print("\n 9. ab mode: Binary data appended successfully.")

file = open("newfile.txt", "x")
file.write("This file is created using x mode.\n")
file.write("It is a new file.")
file.close()

print("File created successfully.")