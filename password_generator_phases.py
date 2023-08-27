from random_word import RandomWords
import random

char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789\?@!#$%&*+=-[] '

print('Welcome to random password generator!')

number_of_passwords_input = input('Amount of passwords: ')
number_of_passwords = int(number_of_passwords_input)

num_of_phases_iput = input('How many phases in the password: ')
num_of_phases = int(num_of_phases_iput)


print('\nHere are your passwords:')

for num in range(number_of_passwords):
    password = ''
    r = RandomWords()
    for p in range(num_of_phases):
        password +=r.get_random_word() + random.choice(char)
    print(password)