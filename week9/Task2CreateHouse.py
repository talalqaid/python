from House import House

def create_houses():
    houses = []
    another = 'y'
    while another.lower() == 'y':
        address = input('Enter the address: ')
        floors = int(input('Enter the number of floors: '))
        doors = int(input('Enter the number of doors: '))
        heating = input('Enter the heating type: ')
        houses.append(House(address, floors, doors, heating))
        another = input("Do you want to add another house? ('y' for yes): ")
    print('No of houses created:', len(houses))
    return houses


if __name__ == '__main__':
    houses = create_houses()
    for house in houses:
        house.print_details()
