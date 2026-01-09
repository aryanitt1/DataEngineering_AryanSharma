length = int(input("Enter minimum length of password required: "))
password = input("Enter a password: ")

specialCharacters = "!@#$%^&*()-_+=<>?/"
digitPresent = 0
specialcharPresent = 0

for char in password:
    if char.isdigit():
        digitPresent = 1
    elif char in specialCharacters:
        specialcharPresent = 1

if (len(password) >= length and digitPresent == 1 and specialcharPresent == 1):
    print("Valid Password")
else:
    print("Invalid Password")
