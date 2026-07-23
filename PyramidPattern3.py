# program to produce following design
# 1  
# 1 2  
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# if user enters n value as 5


num = int(input("Enter the value of n: "))

s = [1, 2, 3, 4, 5]

for i in range(1, num + 1):
    for j in range(i):
        print(s[j], end=" ")
    print()