import random

print("Welcome to the password generator!")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letter = (int(input("How many letters would you like in your password?\n")))
symbol = (int(input("How many symbols would you like in your password?\n")))
number = (int(input("How many number would you like in your password?\n")))

password = []

for char in range(0, letter):
    password += random.choice(letters)

for char in range(0, symbol):
    password += random.choice(symbols)

for char in range(0, number):
    password += random.choice(numbers)

random.shuffle(password)

print(password)

passw = ""

for i in password:
    passw += i

print(passw)