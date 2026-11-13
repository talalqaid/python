# Task 6
def tally_coffees(coffee_orders):
    counts = {}
    for coffee in coffee_orders:
        counts[coffee] = counts.get(coffee, 0) + 1
    return counts

orders = ['Latte', 'Espresso', 'Latte', 'Cappuccino', 'Espresso', 'Latte']
for coffee, total in tally_coffees(orders).items():
    print(coffee, ':', total)
