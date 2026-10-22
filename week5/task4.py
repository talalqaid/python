# Exercise 4: Boolean-returning functions

def is_even(number):
    return number % 2 == 0

def is_negative(number):
    return number < 0

def is_too_big(number):
    return number > 100

def main():
    number = int(input('Enter an integer: '))
    print('Even:', is_even(number))
    print('Negative:', is_negative(number))
    print('Greater than 100:', is_too_big(number))

main()
