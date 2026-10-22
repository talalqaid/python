# Exercise 1: multiplication and average of three numbers

def show_multiplication(x, y):
    print('Product:', x * y)

def show_average(x, y, z):
    print('Average:', (x + y + z) / 3)

def main():
    x = float(input('Enter the first number: '))
    y = float(input('Enter the second number: '))
    show_multiplication(x, y)

    print('Enter three numbers to find their average:')
    a = float(input('First: '))
    b = float(input('Second: '))
    c = float(input('Third: '))
    show_average(a, b, c)
main()
