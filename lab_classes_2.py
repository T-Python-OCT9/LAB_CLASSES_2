from unicodedata import name


class Vehicle :
    brand = ""
    name  = ""
    color = ""
    capacity = ""
    plate_number = ""
    #methods
    def __init__(self, brand : str , name : str, color: str , capacity : str ,plate_number : str ) -> None:
        self.brand = brand
        self.name = name
        self.color = color 
        self.capacity = capacity
        self.plate_number = plate_number

    def drive (self) :
        print(f"the {self.name} is driving!")
    

    def drift (self) : 
      print (f"the {self.name} is drifting !!")

    def carry_cargo(self):
        print(f"the {self.name} is carrying cargo !!") 

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
    
    def drive (self) :
        print(f"the {self.name} is not driving!")
    

  

class Truck(Vehicle):
    
    
    

    def drift (self) : 
      print (f"the {self.name} is not drifting !!")

    

Vehicle1 = Vehicle("ford","mustang","red","five people","5533")

bus1 = Bus  ("toyota" ,"dtsn","white","six people ","9933")

Truck1 = Truck  ("nissan ","Frontier King","Blue","nine people","7733")

Vehicle1.drive()
Vehicle1.drift()
Vehicle1.carry_cargo()

bus1.drive()
bus1.drift()
bus1.carry_cargo()

Truck1.drive()
Truck1.drift()
Truck1.carry_cargo()
