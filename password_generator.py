import random

char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789\?@!#$%&*+=-[] '

print('Welcome to random password generator!')

number_of_passwords_input = input('Amount of passwords: ')
number_of_passwords = int(number_of_passwords_input)

length_of_passwords_iput = input('Password length: ')
length_of_passwords = int(length_of_passwords_iput)

print('\nHere are your passwords:')

for num in range(number_of_passwords):
    password = ''
    for c in range(length_of_passwords):
        password +=random.choice(char)
    print(password)