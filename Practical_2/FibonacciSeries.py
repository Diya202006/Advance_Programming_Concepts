# Program to print Fibonacci series

n = int(input("Enter the value of n: "))

a = 0
b = 1

i = 1

while i <= n:
    print(a)
    c = a + b
    a = b
    b = c
    i = i + 1