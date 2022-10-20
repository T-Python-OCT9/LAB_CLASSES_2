class Vehicle:
    def __init__(self, brand, name, color, capacity, plate_number) -> None:
        self.__brand = brand
        self.__name =  name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number

    def setBrand(self, brand : str):
        if not (isinstance(brand, str)):
            raise ValueError("brand name is must be a string!")
        else:
            self.__brand = brand
    
    def getBrand(self):
        return self.__brand

    def setName(self, name : str):
        if not (isinstance(name, str)):
            raise ValueError("Name is must be a string!")
        else:
            self.__name = name
    
    def getName(self):
        return self.__name
    
    def setColor(self, color : str):
        if not (isinstance(color, str)):
            raise ValueError("Color is must be a string!")
        else:
            self.__color = color
    
    def getColor(self):
        return self.__color
    
    def setCapacity(self, capacity : int):
        if not (isinstance(capacity, int)):
            raise ValueError("Capacity is must be a intger!")
        else:
            self.__capacity = capacity
    
    def getCapacity(self):
        return self.__capacity

    def setPlateNum(self, plate_number : str):
        if not (isinstance(plate_number, str)):
            raise ValueError("Plate number is must be a string!")
        else:
            self.__plate_number = plate_number
    
    def getPlateNum(self):
        return self.__plate_number

    def drive(self):
        print(f"the {self.getName()} is driving!")

    def drift(self):
        if self.getName == "gto 250":
            print(f"the {self.getName()} is drifting !!")
        else:
            print(f"{self.getName()} is not for drifting!")
    def carry_cargo(self):
        if self.getName == "van":
            print(f"the {self.getName()} is carrying cargo !!")
        else:
            print(f"{self.getName()} is not for carrying!")

vehicle1 = Vehicle("ford", "torus", "black", 6, "hel 5000")
vehicle1.drive()
vehicle1.drift()
vehicle1.carry_cargo()

vehicle2 = Vehicle("ferarri", "gto 250", "red", 2, "Nar 0")
vehicle2.drive()
vehicle2.drift()
vehicle2.carry_cargo()

vehicle3 = Vehicle("toyota", "van", "White", 8, "jdi 2665")
vehicle3.drive()
vehicle3.drift()
vehicle3.carry_cargo()
        
class Bus(Vehicle):
    def __init__(self, brand, name, color, capacity, plate_number) -> None:
        super().__init__(brand, name, color, capacity, plate_number)

    def setBrand(self, brand: str):
        super().setBrand(brand)
    
    def getBrand(self):
        return super().getBrand()

    def setName(self, name: str):
        super().setName(name)
    
    def getName(self):
        return super().getName()
    
    def setColor(self, color: str):
        super().setColor(color)
    
    def getColor(self):
        return super().getColor()
    
    def setCapacity(self, capacity: int):
        super().setCapacity(capacity)
    
    def getCapacity(self):
        return super().getCapacity()
    
    def setPlateNum(self, plate_number: str):
        super().setPlateNum(plate_number)
    
    def getPlateNum(self):
        return super().getPlateNum()
    def drive(self):
        super().drive()
    
    def drift(self):
        super().drift()
    
    def carry_cargo(self):
        super().carry_cargo()

#bus1 = Bus(Bus.setBrand(),Bus.setName(),Bus.setColor(),Bus.setCapacity(20),Bus.setPlateNum())

bus1 = Bus("toyota", "Bus", "Black", 20, "bsk 6835")
print(bus1.getBrand())
print(bus1.getName())
print(bus1.getColor())
print(bus1.getCapacity())
print(bus1.getPlateNum())


class Truck(Vehicle):
    def __init__(self, brand, name, color, capacity, plate_number) -> None:
        super().__init__(brand, name, color, capacity, plate_number)

    def getName(self):
        return super().getName()
    def setName(self, name: str):
        super().setName(name)
        print(f"The new Truck name is: {self.getName()}")


    def drive(self):
        print(f"The truck {self.getName()} is driving!, It can carry {self.getCapacity()} cargo!")

    
    
truck1 = Truck("mercedes", "truck", "White", 80, "zhv 9631")
truck1.drive()
truck1.setName("Trruck")
truck1.drive()
truck1.drift()


