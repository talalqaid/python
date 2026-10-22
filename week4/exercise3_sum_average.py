# Exercise 3: Find the total and average of a user-defined count.
count=-1
while count <= 0:
    count = int(input('Please enter a positive number of values: '))
total = 0.0
for counter in range(count):
    number = float(input(f'Enter number {counter + 1}: '))
    total = total + number
average = total / count
print('The total is', total)
print('The average is', average)
