# Program for Run-Length Encoding

string = input("Enter a string: ")

count = 1

for i in range(len(string)):
    if i == len(string) - 1:
        print(string[i] + str(count), end="")
    elif string[i] == string[i + 1]:
        count += 1
    else:
        print(string[i] + str(count), end="")
        count = 1