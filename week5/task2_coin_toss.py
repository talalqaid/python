# Exercise 2: coin tosses and repeated runs of ten
import random

def coin(tosses, show_each=True):
    heads = 0
    tails = 0
    results = []
    for _ in range(tosses):
        result = random.choice(('Heads', 'Tails'))
        if result == 'Heads':
            heads += 1
        else:
            tails += 1
        if show_each:
            print(result)
    return heads, tails

def main():
    tosses = int(input('How many times should the coin be tossed? '))
    if tosses < 0:
        print('The number of tosses cannot be negative.')
        return
    heads, tails = coin(tosses)
    print('Heads:', heads)
    print('Tails:', tails)

    runs = 0
    while True:
        runs += 1
        heads, tails= coin(10, show_each=False)
        if heads == 10 or tails == 10:
            print('It took', runs, 'runs of 10 tosses to get 10 of the same result in a row.')
            print('Winning run:', 'Heads' if heads == 10 else 'Tails')
            break
main()
