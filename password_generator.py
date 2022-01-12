#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Create a list of all the random characters from user input
password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))
for char in range (1, nr_symbols +1):
  password_list.append(random.choice(symbols))
for char in range (1, nr_numbers +1):
  password_list.append(random.choice(numbers))

#Shuffle list
random.shuffle(password_list)


#For loop to take characters from list and put into String
password = ""
for char in password_list:
  password += char

#print output
print(f"Your secure password is: {password}")
