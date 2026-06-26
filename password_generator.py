import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_-+=<>?"

length = int(input("Enter the password length: "))

include_numbers = input("Include numbers? (yes/no): ").lower()

include_symbols = input("Include symbols? (yes/no): ").lower()

characters = letters

if include_numbers == "yes":
    characters += numbers

if include_symbols == "yes":
    characters += symbols

password = ""

for i in range(length):
    password += random.choice(characters)

print("\nYour generated password is:")
print(password)