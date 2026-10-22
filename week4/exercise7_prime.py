# Exercise 7: Determine whether an integer is prime.
from math import isqrt
number = int(input('Enter an integer: '))
is_prime= number >= 2
for divisor in range(2, isqrt(number) + 1):
    if number % divisor == 0:
        print(divisor)
        is_prime = False
        break
if is_prime:
    print(number, 'is prime.')
else:
    print(number, 'is not prime.')
# Try: 77777677777 -> prime.
