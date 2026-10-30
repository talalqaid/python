# Exercise 2(a): Modified version of add_coffee_record.py.
# Add name, quantity, roast and type to coffee.txt.

def main():
    another = 'y'
    coffee_file = open('coffee.txt', 'a')

    while another.lower() == 'y':
        print('Enter the following coffee data:')
        descr = input('Coffee name: ').strip()
        qty = float(input('Quantity (in kg): '))

        roast = input('Roast (dark/medium/light): ').strip().lower()
        while roast not in ('dark', 'medium', 'light'):
            roast = input('Please enter dark, medium or light: ').strip().lower()

        coffee_type = input('Type (beans/ground): ').strip().lower()
        while coffee_type not in ('beans', 'ground'):
            coffee_type = input('Please enter beans or ground: ').strip().lower()

        # Each record uses four lines in this order.
        coffee_file.write(descr + '\n')
        coffee_file.write(str(qty) + '\n')
        coffee_file.write(roast + '\n')
        coffee_file.write(coffee_type + '\n')

        another = input('Add another record? Y = yes, anything else = no: ')

    coffee_file.close()
    print('Data appended to coffee.txt.')
main()
