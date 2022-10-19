
class Vehicle:

    def __init__(self, brand: str, name: str, color: str, capacity : int, plate_number : str) -> None:
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number

    def drive(self)-> str:
        print(f"The vehicle {self.__name} is driving ! ")

    def drift(self)-> str:
        print(f"The vehicle {self.__name} is drifting !!")

    def carry_cargo(self)-> str:
        print(f"The vehicle {self.__name} is carrying a cargo !!")
    
    #Encapsulating brand
    def setBrand(self, brand: str):
        if not isinstance(brand, str):
            raise NameError("The vehicle brand must be String !")
        self.__brand = brand
    def getBrand(self):
        return self.__brand

    #Encapsulating name
    def setName(self, name: str):
        if not isinstance(name, str):
            raise NameError("The vehicle name must be String !")
        self.__name = name
    def getName(self):
        return self.__name
    
    #Encapsulating color
    def setColor(self, color: str):
        if not isinstance(color, str):
            raise NameError("The vehicle color must be String !")
        self.__name = color
    def getColor(self):
        return self.__color
    
    #Encapsulating capacity
    def setCapacity(self, capacity: int):
        if not isinstance(capacity, int):
            raise NameError("The vehicle Capacity must be Integer !")
        self.__name = capacity
    def getCapacity(self):
        return self.__capacity
    
    #Encapsulating plate_number 
    def setPlateNumber(self, plate_number: str):
        if not isinstance(plate_number, int):
            raise NameError("The vehicle plate number must be String !")
        self.__plate_number = plate_number
    def getPlateNumber(self):
        return self.__plate_number


class Bus(Vehicle):

    def __init__(self, brand: str, name: str, color: str, capacity: int, plate_number: str, max_speed : int) -> None:
        super().__init__(brand, name, color, capacity, plate_number)
        self.max_speed = max_speed

    def drive(self):
        return super().drive()

    def drift(self):
        print("The Bus cannot drift !")
    def carry_cargo(self):
        print("The Bus is carrying people on it !")

class Truck(Vehicle):
    def __init__(self, brand: str, name: str, color: str, capacity: int, plate_number: str, carry_weight : float) -> None:
        super().__init__(brand, name, color, capacity, plate_number)
        self.carry_weight = carry_weight

    def drive(self):
        return super().drive()

    def drift(self):
        print("The Truck Cannot drift !")

    def carry_cargo(self):
        return super().carry_cargo()
        

bus1 = Bus("Bus", "Y1","Yellow",30, "SSS123", 110)
truck1 = Truck("Truck", "T1", "Grey", 3,"TTT111",10000)

bus1.drive()
bus1.drift()
bus1.carry_cargo()

truck1.drive()
truck1.drift()
truck1.carry_cargo()



