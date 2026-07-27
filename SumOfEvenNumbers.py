# Program to find the sum of even numbers up to n

n = int(input("Enter the value of n: "))

i = 2
sum = 0

while i <= n:
    sum = sum + i
    i = i + 2

print("Sum =", sum)