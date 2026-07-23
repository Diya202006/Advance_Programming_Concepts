# Print Odd Numbers from 1 to n

num = int(input("Enter the Number: "))

for i in range(1, num + 1):
    if i % 2 != 0:
        print(i)