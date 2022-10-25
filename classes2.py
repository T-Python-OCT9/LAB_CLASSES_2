class Veichle:

    def __init__(self, brand:str, name:str , color : str, capacity : int, plate_number: str) -> None:
        self.__name = name
        self.__brand = brand
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number
    


    #definig a getter for name
    def getName(self):
        return self.__name
    
    #defining a setter
    def setName(self, name):
        self.__name = name

    def drive(self) -> None:
        print(f"the car {self.getName()} is driving")

    
    def drift(self) ->None:
        print(f"the car is {self.getName()} is drifting")

    
    def carry_cargo(self) -> None:
        print(f"the {self.getName()} is carrying cargo")

    

class Bus(Veichle):
    
    def drift(self) -> None:
        print(f"the {self.getName()} cannot drift !!")

    def carry_cargo(self) -> None:
        print(f"the {self.getName()} cannot carry cargo")

class Truck(Veichle):
    
    def drift(self) -> None:
        print(f"the truck {self.getName()} cannot drift")



veichle1 = Veichle("Chevrolet", "Caprice", "Paige", 5, "ABB 457")
bus1 = Bus("Mercedes", "C1", "white", 32, "BDC 3847")
truck1 = Truck("Ford", "F1", "Black", 4, "ERC 3467")

veichle1.drive()
veichle1.drift()
veichle1.carry_cargo()

bus1.drive()
bus1.drift()
bus1.carry_cargo()

truck1.drive()
truck1.drift()
truck1.carry_cargo()