from tokenize import Name
from unicodedata import name


class Vehicle :

    def __init__(self, brand : str, name : str, color : str, capacity : str , plate_number : int) -> None:
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate = plate_number

    def drive(self):
        return f"the {self.__name} is driving !!"

    def drift(self):
        return f"the {self.__name} is drifting !!"

    def carry_cargo(self):
        return f"the {self.__name} is carrying cargo !!"

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


class Bus(Vehicle) :
    car1= Vehicle("ford","vectoria","Blue","rr",12345)
    print(car1.drift())



class Truck(Vehicle) :
    car2= Vehicle("niesan","ddsen","wihgt","ii",518)
    print(car2.drive())


car1= Vehicle("tayota","camry","black","pp",555)
bus1= Bus("ford","siera","black","ofo",122)
tracck= Truck("eico","opa","blue","poop",224)


print(car1.drift())
print(car1.drive())
print(car1.carry_cargo())

print(bus1.drift())
print(bus1.drive())
print(bus1.carry_cargo())

print(tracck.drift())
print(tracck.drive())
print(tracck.carry_cargo())