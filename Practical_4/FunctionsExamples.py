# Check wheather the Number is Even or Odd by using Function
 
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


num = int(input("Enter a number: "))

result = check_even_odd(num)

print("The number is", result)