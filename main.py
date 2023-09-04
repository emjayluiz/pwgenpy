#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
numL = 0
symb = 0
numN = 0
password = ""
for x in letters:
    if numL < nr_letters:
        x = random.choice(letters)
        numL += 1
        password += x

for y in symbols:
    if symb < nr_symbols:
        y = random.choice(symbols)
        symb += 1
        password += y

for z in numbers:
    if numN < nr_numbers:
        y = random.choice(numbers)
        numN += 1
        password += z
print(password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# In this code, we initialize an empty string randomized_password
# to store the randomized characters. Then, in each iteration of the loop,
# we generate a random index within the range of the remaining characters in password.
# We extract the character at that index and append it to randomized_password.
# , we update password by removing the selected character,
# ensuring that it won't be selected again in the next iteration.


randomized_password = ""
for rpw in range(len(password)):
    rpw = random.randint(0, len(password) - 1)
    randomized_password += password[rpw]
    password = password[:rpw] + password[rpw+1:]
print(randomized_password)