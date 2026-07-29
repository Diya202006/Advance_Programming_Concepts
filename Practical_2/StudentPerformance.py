# Program to evaluate student performance

per = float(input("Enter the percentage: "))

if per >= 90:
    print("Excellent Performance")
elif per >= 80:
    print("Very Good Performance")
elif per >= 70:
    print("Good Performance")
elif per >= 60:
    print("Average Performance")
else:
    print("Poor Performance")