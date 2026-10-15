# Exercise 9(b): Keep guessing until correct.
from random import randint
n = randint(1, 20)
guess = int(input('Guess the number (1-20): '))
while guess != n:
    if guess < n:
        print('Higher')
    else:
        print('Lower')
    guess = int(input('Guess the number (1-20): '))
print('You guessed it!')
