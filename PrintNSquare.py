# Print the Data 1, 2, 4, 8, 16, 32,.......,n^2

num = int(input("Enter the number: "))

for i in range(num + 1):
    i = 2 ** i
    print(i)