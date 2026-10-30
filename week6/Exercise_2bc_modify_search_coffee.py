# Exercises 2(b) and 2(c): Modified version of modify_coffee_records.py.
# Choose to modify quantity, roast and type, or list dark-roast coffees.
import os

def modify_record():
    found = False
    search = input('Enter a coffee name to modify: ').strip()
    new_qty = float(input('Enter the new quantity (kg): '))
    new_roast = input('Enter new roast (dark/medium/light): ').strip().lower()
    while new_roast not in ('dark', 'medium', 'light'):
        new_roast = input('Please enter dark, medium or light: ').strip().lower()
    new_type = input('Enter new type (beans/ground): ').strip().lower()
    while new_type not in ('beans', 'ground'):
        new_type = input('Please enter beans or ground: ').strip().lower()

    coffee_file = open('coffee.txt', 'r')
    temp_file = open('temp.txt', 'w')
    descr = coffee_file.readline()
    while descr != '':
        qty = float(coffee_file.readline())
        roast = coffee_file.readline().rstrip('\n')
        coffee_type = coffee_file.readline().rstrip('\n')
        descr = descr.rstrip('\n')

        if descr.lower() == search.lower():
            qty, roast, coffee_type = new_qty, new_roast, new_type
            found = True

        temp_file.write(descr + '\n')
        temp_file.write(str(qty) + '\n')
        temp_file.write(roast + '\n')
        temp_file.write(coffee_type + '\n')
        descr = coffee_file.readline()

    coffee_file.close()
    temp_file.close()
    os.replace('temp.txt', 'coffee.txt')
    print('The file has been updated.' if found else 'That item was not found in the file.')

def search_dark_roasts():
    coffee_file = open('coffee.txt', 'r')
    names = []
    descr = coffee_file.readline()
    while descr != '':
        qty = float(coffee_file.readline())
        roast = coffee_file.readline().rstrip('\n')
        coffee_type = coffee_file.readline().rstrip('\n')
        if roast.lower() == 'dark':
            names.append(descr.rstrip('\n'))
        descr = coffee_file.readline()
    coffee_file.close()
    print('Number of dark roast coffee records:', len(names))
    print('Names:', ', '.join(names) if names else 'None')

def main():
    choice = input('Enter M to modify or S to search dark roasts: ').strip().lower()
    if choice == 'm':
        modify_record()
    elif choice == 's':
        search_dark_roasts()
    else:
        print('Invalid choice.')
main()
