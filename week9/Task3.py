from Task2CreateHouse import create_houses

houses = create_houses()
address = input('Enter the address of the house you want to search for: ')

for house in houses:
    if house.address.strip().lower() == address.strip().lower():
        print('House found!')
        house.print_details()
        break
else:
    print('House not found!')
