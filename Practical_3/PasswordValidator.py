# Program to validate a password

password = input("Enter your password: ")

uppercase = 0
lowercase = 0
digit = 0
special = 0

for ch in password:
    if 'A' <= ch <= 'Z':
        uppercase += 1
    elif 'a' <= ch <= 'z':
        lowercase += 1
    elif '0' <= ch <= '9':
        digit += 1
    else:
        special += 1

if len(password) >= 8 and uppercase >= 1 and lowercase >= 1 and digit >= 1 and special >= 1:
    print("Valid Password")
else:
    print("Invalid Password")