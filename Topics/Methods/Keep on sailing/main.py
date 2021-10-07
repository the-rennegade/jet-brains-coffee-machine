# our class Ship
class Ship:
    def __init__(self, name, capacity, destination):
        self.name = name
        self.capacity = capacity
        self.cargo = 0
        self.destination = destination

    def sail(self):
        print(f'The {self.name} has sailed for {self.destination}!')

name_input = input()
destination_input = input()

ship_object = Ship(name_input, 800, destination_input)

ship_object.sail()
