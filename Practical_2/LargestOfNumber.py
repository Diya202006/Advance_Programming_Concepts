# Program to find the largest of n numbers

n = int(input("Enter how many numbers: "))

largest = int(input("Enter number 1: "))

i = 2

while i <= n:
    num = int(input("Enter number: "))
    
    if num > largest:
        largest = num
        
    i = i + 1

print("Largest number =", largest)