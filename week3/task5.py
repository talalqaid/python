
# Exercise 5 - Nail Order Calculator

nails = int(input("Enter the number of nails: "))

price_per_nail = 0.10
postage = 2.00

if nails <= 0:
    print("Please enter a positive number of nails.")
else:
    if nails <= 50:
        discount = 0
    elif nails <= 100:
        discount = 10
    elif nails <= 200:
        discount = 20
    else:
        discount = 25

    original_cost = nails * price_per_nail
    discount_amount = original_cost * discount / 100
    discounted_cost = original_cost - discount_amount
    total = discounted_cost + postage

    print(f"Discount applied: {discount}%")
    print(f"Original order cost: £{original_cost:.2f}")
    print(f"Cost after discount: £{discounted_cost:.2f}")
    print(f"Total bill including postage: £{total:.2f}")
