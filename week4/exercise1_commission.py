# Exercise 1: Accept y/Y and add a bonus for sales over £5000.
keep_going = 'y'
while keep_going.lower() == 'y':
    sales = float(input('Enter the amount of sales:'))
    comm_rate = float(input('Enter the % commission rate:'))
    commission = sales * comm_rate / 100
    if sales > 5000:
        commission += 50
    print(f'The commission is £{commission:.2f}')
    keep_going = input('Calculate another commission? (y/Y for yes): ')
print('OK - goodbye.')
