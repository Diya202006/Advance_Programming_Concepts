# Program to find the sum of natural numbers up to n

n = int(input("Enter the value of n: "))

i = 1
sum = 0

while i <= n:
    sum = sum + i
    i = i + 1

print("Sum =", sum)