# Exercise 9(a): One guess only.
from random import randint
n = randint(1, 20)
guess = int(input('Guess the number (1-20): '))
if guess < n:
    print('Higher')
elif guess > n:
    print('Lower')
else:
    print('You guessed it!')
