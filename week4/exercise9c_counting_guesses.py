# Exercise 9(c): Count attempts until correct.
from random import randint
n = randint(1, 20)
attempts = 0
while True:
    guess = int(input('Guess the number (1-20): '))
    attempts += 1
    if guess < n:
        print('Higher!')
    elif guess > n:
        print('Lower!')
    else:
        print(f'You guessed it in {attempts} tries!')
        break
