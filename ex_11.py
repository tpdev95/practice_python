"""Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list."""

import random
import string

letters = string.ascii_letters

how_strong = input("How strong want your password? weak or strong: ")

password = str(random.randint(1,48))

# print(password)

if how_strong == "weak":
    pwd_length = 6
elif how_strong == "strong":
    pwd_length = 10
else:
    how_strong = input("Only weak or strong: ")
    pwd_length = 6

while len(password) < pwd_length:
    first = letters[random.randint(1,48)].capitalize()
    cont = letters[random.randint(1,48)]
    num_string = str(random.randint(1,99))
    password = first + password + cont + num_string

print("your password is "+password)
# print(letters)
#
# while len(weak_password) < 6 and len(strong_password) < 8:
#     if how_strong == "weak":
#         weak_password.join(random.choice(letters))
#         print("Your password is"+weak_password)
#     elif how_strong == "strong":
#         strong_password.join(random.choice(letters))
#         print("Your password is"+weak_password)
#     else:
#         how_strong = input("Only weak or strong: ")
# # return ''.join(random.choice(letters)) for i in range(stringLength)
#
# if __name__=="__main__":
#     print(randomString(5))
#     how_strong = input("How strong want your password? weak or strong: ")
#     #
#     # if how_strong == "weak":
#     #     weak
