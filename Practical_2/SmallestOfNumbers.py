# Program to find the smallest of n numbers

n = int(input("Enter how many numbers: "))

smallest = int(input("Enter number 1: "))

i = 2

while i <= n:
    num = int(input("Enter number: "))
    
    if num < smallest:
        smallest = num
        
    i = i + 1

print("Smallest number =", smallest)