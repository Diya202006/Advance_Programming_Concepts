import re
 
def extract_phone_numbers(text):
    pattern = r'\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}'
    phone_numbers = re.findall(pattern, text)
    return phone_numbers
 
text = input("Enter a block of text:\n")

numbers = extract_phone_numbers(text)

if numbers:
    print("\nPhone Numbers Found:")
    for number in numbers:
        print(number)
else:
    print("No valid phone numbers found.")