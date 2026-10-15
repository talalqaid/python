# Exercise 8: Compound investment returns for four years.
initial = float(input('Enter your initial investment amount:'))
balance = initial
rates = [0.05, 0.07, 0.10, 0.30]
for year in range(4):
    balance = balance + balance * rates[year]
    print(f'Year {year + 1}: Balance = £{balance:.2f}')
print(f'\nTotal value after 4 years: £{balance:.2f}')
print(f'You made a profit of £{balance - initial:.2f}')
