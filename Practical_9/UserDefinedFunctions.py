# Defining a user-defined function
 
def message():
    print("Welcome to Python")
 
def add(a, b):
    print("Addition =", a + b)
 
def square(n):
    return n * n
 
def greet(name="Student"):
    print("Hello", name)
 
message()

add(10, 20)

result = square(5)
print("Square =", result)

greet()
greet("Diya")