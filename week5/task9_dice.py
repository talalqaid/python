# Exercise 9: roll a user-specified number of six-sided dice
import random

def main():
    number = int(input('How many dice would you like to throw? '))
    if number < 1:
        print('Enter at least one die.')
        return
    total = 0
    for i in range(number):
        score = random.randint(1, 6)
        total += score
        print(f'Die {i + 1}: {score}')
    print('Total score:', total)
main()
