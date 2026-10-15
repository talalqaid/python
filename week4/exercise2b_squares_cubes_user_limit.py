# Exercise 2(b): Let the user specify the maximum number.
maximum = int(input('Enter the largest number: '))
print('Number\tSquare\tCube')
for number in range(1, maximum + 1):
    print(f'{number}\t{number ** 2}\t{number ** 3}')
