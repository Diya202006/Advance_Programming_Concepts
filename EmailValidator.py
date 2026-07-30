# Program to validate an email address

email = input("Enter an email address: ")

at = 0
dot = 0
at_pos = -1
dot_pos = -1

for i in range(len(email)):
    if email[i] == '@':
        at += 1
        at_pos = i
    elif email[i] == '.':
        dot += 1
        dot_pos = i

if at == 1 and dot >= 1 and at_pos > 0 and dot_pos > at_pos + 1 and dot_pos < len(email) - 1:
    print("Valid Email")
else:
    print("Invalid Email")