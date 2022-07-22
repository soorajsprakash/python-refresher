# --------------------------------------------------------------
# -------------------- PASSWORD GENERATOR ----------------------
# -------------------------- (LOOPS) ---------------------------
# --------------------------------------------------------------

#Eazy Level - Order not randomised:
              #e.g. 4 letter, 2 symbol, 2 number ===> JduE&!91
#Hard Level - Order of characters randomised:
              #e.g. 4 letter, 2 symbol, 2 number ===> g^2jk8&P

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []
for a in range(0, nr_letters):
    password_list.append(random.choice(letters))
for a in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
for a in range(0, nr_numbers):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)
print(password_list)
pwd = ""
for i in password_list:
    pwd += i

print(f"Your password is: {pwd}")


# -------- OLD STEPS ----------
# --- FIRST METHOD ---
# password = ""
# for a in range(0, nr_letters):
#     randomLetterIndex = random.randint(0, len(letters)-1)
#     password += letters[randomLetterIndex]
# for b in range(0, nr_symbols):
#     randomSymIndex = random.randint(0, len(symbols)-1)
#     password += symbols[randomSymIndex]
# for c in range(0, nr_numbers):
#     randomNumIndex = random.randint(0, len(numbers)-1)
#     password += numbers[randomNumIndex]
# print(password)

# --- SECOND METHOD ---
# password = ""
# for a in range(0, nr_letters):
#     password += random.choice(letters)
# for a in range(0, nr_symbols):
#     password += random.choice(symbols)
# for a in range(0, nr_numbers):
#     password += random.choice(numbers)
# print(password)

# --- THIRD METHOD (INCOMPLETE)---
# pwdOptions = [letters, symbols, numbers]
# userChoice = [nr_letters, nr_symbols, nr_numbers]
# password=""

# for a in userChoice:
#     # print(a)
    
#     for b in pwdOptions:
#         a -= 1
#         randomIndex  = random.randint(0, len(b)-1)
#         password += b[randomIndex]