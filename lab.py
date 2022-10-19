class Vehicle:

    def __init__(self, brand: str, name: str, color: str, capacity: str, plate_number: str):
        self.brand = brand
        self.name = name
        self.color = color
        self.capacity = capacity
        self.plate_number = plate_number

    # methods
    def drive(self):
        print(f"the {self.name} is driving!")

    def drift(self):
        print(f"the {self.name} is drifting !!") 

    def carry_cargo(self):
        print(f"the {self.name} is carrying cargo !!")
    
    # geter and seter for each attribute
    def set_brand(self, brand):
        self.brand = brand
    
    def get_brand(self):
        return f'the brand is: {self.brand}'

    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return f'the name is: {self.name}'
    
    def set_color(self, color):
        self.color = color
    
    def get_color(self):
        return f'the color is: {self.color}'
    
    def set_capacity(self, capacity):
        self.capacity = capacity
    
    def get_capacity(self):
        return f'the capacity is: {self.capacity}'
    
    def set_plate_number(self, plate_number):
        self.plate_number = plate_number
    
    def get_plate_number(self):
        return f'the plate_number is: {self.plate_number}'

# subclasses
class Bus(Vehicle):
    
    def drift(self):
        print(f"the {self.name} doesn't drift !!")

class Truck(Vehicle):
    pass


vehicle1 = Vehicle('ferrari','pista 488','red','2', 'F488') # object
# call all the methods for vehicle1
vehicle1.drive()
vehicle1.drift()
vehicle1.carry_cargo()

bus1 = Bus('nissan', 'x11', 'white', '10', '10022') # object
# call all the methods for bus1
bus1.drive()
bus1.drift()
bus1.carry_cargo()

truck1 = Truck('ford', 'rapter', 'black', '4', '10011') # object
# call all the methods for truck1
truck1.drive()
truck1.drift()
truck1.carry_cargo()
    
    

    


