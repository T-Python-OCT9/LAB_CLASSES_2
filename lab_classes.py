'''
Define a vehicle class. It has the following structure:
# (properties): brand, name, color, capacity, plate_number.
# (methods):
    - drive() prints "The vehicle_name is driving!"
    - drift() prints "The vehicle_name is drifting!" or something else depending on the class.
    - carry_cargo() prints "The vehicle_name is carrying cargo!" or something else depending on the class.
# For each of the properties do a setter & getter (encabsulate the data).
# Create two other subclasses (inherit from vehicle): Bus, Truck.
Note:
    Override the methods as needed for each subclass of vehicle.
    Create at least one object of each class.
    Call all the methods on each object.
'''


class Vehicle:
    def __init__(self, name: str, brand: str, color: str, capacity: int, plate_number: str) -> None:
        self.__name = name
        self.__brand = brand
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number

    def setName(self, name: str):
        if not (isinstance(name, str)):
            raise ValueError("Only string type accepted for name.")
        self.__name = name

    def getName(self):
        return self.__name

    def setBrand(self, brand: str):
        if not (isinstance(brand, str)):
            raise ValueError("Only letters accepted.")
        self.__brand = brand

    def getBrand(self):
        return self.__brand

    def setColor(self, color: str):
        if not (isinstance(color, str)):
            raise ValueError("Only letters accepted.")
        self.__color = color

    def getColor(self):
        return self.__color

    def setCapacity(self, capacity: int):
        if not (isinstance(capacity, int) and capacity > 2):
            raise ValueError("Only numbers accepted for capacity and must be 2 seats and more.")
        self.__capacity = capacity

    def getCapacity(self):
        return self.__capacity

    def setPlateNumber(self, plate_number: str):
        if not (isinstance(plate_number, str) and len(plate_number) == 6):
            raise ValueError("Only 6 charachters accepted.")
        self.__plate_number = plate_number

    def getPlateNumber(self):
        return self.__plate_number

    def drive(self):
        print(f"The {self.__name} is driving!")

    def drift(self):
        print(f"The {self.__name} is drifting!")

    def carryCargo(self):
        print(f"The {self.__name} is carrying cargo!")


class Bus(Vehicle):
    def carryCargo(self):
        print(f"Depends on capacity of bus: {self.getName()}, Carrgo  trunk maybe full!")

    def drift(self):
        print(f"The bus: {self.getName()} can't drift!")


class Truck(Vehicle):
    def carryCargo(self):
        print(f"The truck: {self.getName()}, can carry {self.getCapacity()} cargo!")

    def drift(self):
        print(f"The truck: {self.getName()} will never drift!")


bus1 = Bus('Z6', 'ISUZO', 'Yellow', 25, 'SEU861')
truck1 = Truck('CNG TRUCK', 'MERCEDES', 'RED', 100, 'LEU326')

bus1.drive()
bus1.drift()
bus1.carryCargo()

truck1.drive()
truck1.drift()
truck1.carryCargo()
