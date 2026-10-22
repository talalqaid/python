# Exercise 3: temperature conversion tables

def fahrenheit(temp):
    return temp * 1.8 + 32

def centigrade(temp):
    return (temp - 32) * 5 / 9

def main():
    print('Centigrade to Fahrenheit')
    print('C\tF')
    for temp in range(0, 101, 10):
        print(f'{temp}\t{fahrenheit(temp):.2f}')

    print('\nFahrenheit to Centigrade')
    print('F\tC')
    for temp in range(0, 101, 10):
        print(f'{temp}\t{centigrade(temp):.2f}')

main()
