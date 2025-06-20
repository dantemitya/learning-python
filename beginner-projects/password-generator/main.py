""" Generates random passwords with customizable length 
and character types (e.g. include digits, symbols). """

# for choosing random characters
from random import choice

print("====PASSWORD GENERATOR====")

# create the list of possible character for random.choice to choose from
chars = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXYZ0123456789!@#$%^&*()[]-"""
chars = list(chars)
test = choice(chars)

# allow the user to specify how long they wish their password to be
password_length = int(input("How long would you like you password to be (8-128 chars): "))
print()
password = []

# output the password as a string
for char in range(password_length):
    password.append(choice(chars))
print(f"Your password is: {''.join(password)}")
print()
