# program to produce following design
# 1  
# 2 2   
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 
# if user enters n value as 5

# Program to print the pattern

n = int(input("Enter the value of n: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()