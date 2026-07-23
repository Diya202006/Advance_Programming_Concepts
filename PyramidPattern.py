# program to produce following design
# A  
# A B  
# A B C
# A B C D
# A B C D E
# if user enters n value as 5

num = int(input("Enter the value of n: "))

for i in range(1, num + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()