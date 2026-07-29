# Program to check whether a number is prime or not

n = int(input("Enter a number: "))

count = 0
i = 1

while i <= n:
    if n % i == 0:
        count = count + 1
    i = i + 1

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")