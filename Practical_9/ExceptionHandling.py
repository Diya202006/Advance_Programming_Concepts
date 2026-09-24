# Exception Handling(try, except, else, finally)

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter numbers only.")

else:
    print("Division is successful.")
    print("Result =", result)

finally:
    print("This is the finally block.")
    print("Program execution completed.")