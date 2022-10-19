from unicodedata import name


class Vehicle :
   
    #methods
    def __init__(self, brand : str , name : str, color: str , capacity : str ,plate_number : str ) -> None:
        self.__brand = brand
        self.__name = name
        self.__color = color 
        self.__capacity = capacity
        self.__plate_number = plate_number

    def drive (self) :
        print(f"the {self.__name} is driving!")
    

    def drift (self) : 
      print (f"the {self.__name} is drifting !!")

    def carry_cargo(self):
        print(f"the {self.__name} is carrying cargo !!") 

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
        self.capacity = capacity

    def get_capacity(self):
        return f'the capacity is: {self.__capacity}'

    def set_plate_number(self, plate_number):
        self.__plate_number = plate_number

    def get_plate_number(self):
        return f'the plate_number is: {self.__plate_number}'

# subclasses
class Bus(Vehicle):
    
    def drive (self) :
        print(f"the bus is not driving!")
    

  

class Truck(Vehicle):
    
    
    

    def drift (self) : 
      print (f"the truck is not drifting !!")

    

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
