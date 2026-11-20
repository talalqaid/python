class House:
    def __init__(self, address, floors, doors, heating):
        self.address = address
        self.floors = floors
        self.doors = doors
        self.heating = heating

    def print_details(self):
        print('Address:', self.address)
        print('No of floors:', self.floors)
        print('No of doors:', self.doors)
        print('Heating:', self.heating)
