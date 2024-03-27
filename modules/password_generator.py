import random, string
import os

def password_generator_level1():
    password = ''
    for i in range(8):
        start = random.random()
        if start >= 0.5:
            char = random.randint(0, 9)
            password = password + str(char)
        elif start < 0.5:
            char = random.choice(string.ascii_letters)
            password = password + str(char)

    print('Generated a Random 8 Character String...')
    return password

## Doubles the length of the password.
def password_generator_level2(password):
    for i in range(8):
        start = random.random()
        if start >= 0.5:
            char = random.randint(0, 9)
            password = password + str(char)
        elif start < 0.5:
            char = random.choice(string.ascii_letters)
            password = password + str(char)

    print('Adding 8 Characters to your Password...')
    return password

## Adds 4 random symbols to the end of the password.
def password_generator_level3(password):

    for i in range(4):
        padding = random.choice("`~!@#$%^&*()-_=+\|]}[{;:,<.>/?")
        password = password + padding

    print('Adding 4 Random Symbols to the end of your Password...')
    return password

## Adds 4 random symbols to the start of the password.
def password_generator_level4(password):
    for i in range(4):
        padding = random.choice("`~!@#$%^&*()-_=+\|]}[{;:,<.>/?")
        password = padding + password

    print('Adding 4 Random Symbols to the start of your Password...')
    return password

## Randomises order of the password.
def password_generator_level5(password):
    print(password)
    password = ''.join(random.sample(password, len(password)))

    print('Randomising the order of your Password...')
    return password

def primary_password_generator():
    return password_generator_level5(password_generator_level4(password_generator_level3(password_generator_level2(password_generator_level1()))))