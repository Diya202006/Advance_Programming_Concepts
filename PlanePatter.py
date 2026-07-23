# Program to print:
# A B C
# A B C
# A B C

Letter = ["A", "B", "C"]
for i in range(3):
    for j in Letter:
        print(j, end=" ")
    print()