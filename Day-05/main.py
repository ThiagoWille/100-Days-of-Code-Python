#Minha tentativa (Funcional)
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nbr_letters = int(input("How many letters would you like in you password?\n"))
nbr_numbers = int(input("How many numbers would you like?\n"))
nbr_symbols = int(input("How many symbols would you like?\n"))

password = ""

for char in range(1, (nbr_letters+1)):
    password += random.choice(letters)
for char in range(1, (nbr_numbers+1)):
    password += random.choice(numbers)
for char in range(1, (nbr_symbols+1)):
    password += random.choice(symbols)

passw = list(password)

final_psw = ""
random.shuffle(passw)

for rand in passw:
    final_psw += rand

print(f"You new password is: {final_psw}")

#Acompanhando a Professora

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nbr_letters = int(input("How many letters would you like in you password?\n"))
nbr_numbers = int(input("How many numbers would you like?\n"))
nbr_symbols = int(input("How many symbols would you like?\n"))

password_list = []

for char in range(0, nbr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nbr_numbers):
    password_list.append(random.choice(numbers))

for char in range(0, nbr_symbols):
    password_list.append(random.choice(symbols))

print(password_list)

random.shuffle(password_list)

pswrd = ""
for char in password_list:
    pswrd += char

print(f"You new password is: {pswrd}")