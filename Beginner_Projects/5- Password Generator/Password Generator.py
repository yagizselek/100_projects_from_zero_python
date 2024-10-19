import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

random_vars = [[], [], []]
#first letter
#second symbol
#third number
for x in range(0, nr_letters):
    a = random.choice(letters)
    random_vars[0].append(a)

for x in range(0, nr_symbols):
    a = random.choice(symbols)
    random_vars[1].append(a)

for x in range(0, nr_numbers):
    a = random.choice(numbers)
    random_vars[2].append(a)

flatten_random_vars = []

for x in range(0, 3):
    a = random_vars[x]
    for y in a:
        flatten_random_vars.append(y)

random.shuffle(flatten_random_vars)

password = ""

for x in flatten_random_vars:
    password += x

print(f"Your password is {password}")

#My mistake : I could use a list instead of list of lists because they are all string.