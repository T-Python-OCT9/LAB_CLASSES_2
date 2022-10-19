# define a Vehicle class . it has the following structure :
# definig a class in python

class Vehicle:

    # class attribute
    kind = "car"

    def __init__(self, brand: str, name: str, color: str, capacity: str, plate_number: str) -> None:
        # initilizing the class
        # instance attributes / properties
        # private instance attribute
        self.__brand = brand
        # private instance attribute
        self.__name = name
        # private instance attribute
        self.__color = color
        # private instance attribute
        self.__capacity = capacity
        # private instance attribute
        self.__plate_number = plate_number

     # definig a setter for the private attribute for brand

    def setbrand(self, brand: str) -> str:
        if not (isinstance(brand, str) and len(str(brand)) >= 5):
            raise ValueError(" brand must be string and more 5 places")
        self.__brand = brand

        # define a getter for the private attribute

    def getbrand(self):
        return self.__brand

    # definig a setter for the private attribute for name

    def setname(self, name: str) -> str:
        if not (isinstance(name, str) and len(str(name)) == 6):
            raise ValueError(" name must be string and more 10 places")
        self.__name = name

     # define a getter for the private attribute

    def getname(self):
        return self.__name

      # definig a setter for the private attribute for color

    def setcolor(self, color: str) -> str:
        if not (isinstance(color, str) and len(str(color)) >= 3):
            raise ValueError(" color must be string and more 3 places")
        self.__color = color

    # define a getter for the private color

    def getcolor(self):
        return self.__color

    # definig a setter for the private attribute for capacity

    def setcapacity(self, capacity: str) -> str:
        if not (isinstance(capacity, str) and len(str(capacity)) >= 5):
            raise ValueError(" capacity must be string and more 5 places")
        self.__capacity = capacity

        # define a getter for the private attribute capacity

    def getcapacity(self):
        return self.__capacity

    # definig a setter for the private attribute for plate_number

    def setplate_number(self, plate_number: str) -> str:
        if not (isinstance(plate_number, int) and len(int(plate_number)) >= 10):
            raise ValueError(" plate_number must be string and more 10 places")
        self.__plate_number = plate_number

        # define a getter for the private attribute plate_number

    def getplate_number(self):
        return self.__plate_number

    def drive(self) -> str:
        return f"the {self.__name} is driving!"

    def drifting(self) -> str:
        return f"the {self.__name} is drifting !!"

    def carry_cargo(self) -> str:
        return f"the {self.__name} is carrying cargo !!"

# inheritance


class Bus(Vehicle):
    def drifting(self) -> str:
        return f"the {self.getname()} is drifting !!"


class Truck(Vehicle):
    def carry_cargo(self) -> str:
        return f"the {self.getname()} is carrying cargo !!"


car1 = Vehicle("dvbsdf", "asdfsdf", "red ", "sdfgh", "1234567")
print(car1.drive())
print(car1.drifting())
print(car1.carry_cargo())

car2 = Bus("BBBBB", "aJJJJJNNN", "red ", "sdfgh", "1234567")
print(car2.drifting())


car3 = Truck("sdfgh", "sdcfvgbhj", "red ", "sdfghj", "1234567")
print(car3.carry_cargo())
