class Vehicle:

    def __init__(self, brand: str, name: str, color: str, capacity: str, plate_number: str):
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number


    # geter and seter for each attribute
    def set_brand(self, brand):
        self.__brand = brand
    
    def get_brand(self):
        return f'the brand is: {self.__brand}'

    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return f'the name is: {self.__name}'
    
    def set_color(self, color):
        self.__color = color
    
    def get_color(self):
        return f'the color is: {self.__color}'
    
    def set_capacity(self, capacity):
        self.__capacity = capacity
    
    def get_capacity(self):
        return f'the capacity is: {self.__capacity}'
    
    def set_plate_number(self, plate_number):
        self.__plate_number = plate_number
    
    def get_plate_number(self):
        return f'the plate_number is: {self.__plate_number}'
    
     # methods
    def drive(self):
        print(f"the {self.get_name()} is driving!")

    def drift(self):
        print(f"the {self.get_name()} is drifting !!") 

    def carry_cargo(self):
        print(f"the {self.get_name()} is carrying cargo !!")

# subclasses
class Bus(Vehicle):
    
    def drift(self):
        print(f"the {self.get_name()} doesn't drift !!")

class Truck(Vehicle):
    pass


vehicle1 = Vehicle('ferrari','pista 488','red','2', 'F488') # object
# call all the methods for vehicle1
print("---vehicle class metods---")
vehicle1.drive()
vehicle1.drift()
vehicle1.carry_cargo()

bus1 = Bus('nissan', 'x11', 'white', '10', '10022') # object
# call all the methods for bus1
print("---bus class metods---")
bus1.drive()
bus1.drift()
bus1.carry_cargo()

truck1 = Truck('ford', 'rapter', 'black', '4', '10011') # object
# call all the methods for truck1
print("---truck class metods---")
truck1.drive()
truck1.drift()
truck1.carry_cargo()
    
    

    


