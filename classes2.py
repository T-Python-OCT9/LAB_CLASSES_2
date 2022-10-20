class Vehicle:

      #initilizing 
    def __init__(self, name : str, brand : str, color : str,capacity :str,plate_number:str) -> None:
        self.__name=name
        self.__brand=brand
        self.__color=color
        self.__capacity= capacity
        self.__plate_number=plate_number

    #instance properties
    def drive(self):
        return f"the {self.__name} is driving!"
    
    def drift(self):
        return f"the {self.__name}  is drifting !!"
    
    def carry_cargo(self):
        return f"the {self.__name} is not carrying cargo !!"

    #define a setter
    def setname(self, name):
        if not  (isinstance(name, str) and len(name) <10):
            raise ValueError("name must be string and less than 10 places")
        self.__name = name
    def setcapacity(self, capacity):
        if not  (isinstance(capacity, str) and len(capacity) <10):
            raise ValueError("capacity must be integer and less than 10 places")
        self.__capacity= capacity
    def setbrand(self, brand):
        if not  (isinstance(brand, str) and len(brand) <10):
            raise ValueError("brand must be string and less than 10 places")
        self.__brand = brand
    def setcolor(self,color):
        if not  (isinstance(color, str) and len(color) <10):
            raise ValueError("color must be string and less than 10 places")
        self.__color = color
    def setplate_number(self, plate_number):
        if not  (isinstance(plate_number, str) and len(plate_number) <10):
            raise ValueError("Plate number must be string and less than 10 places")
        self.__plate_number = plate_number

    #define a getter
    def getname(self):
        return self.__name
    def getcpacity(self):
        return self.__capacity
    def getbrand(self):
        return self.__brand
    def getcolor(self):
        return self.__color
    def getplate_number(self):
        return self.__plate_number

class bus(Vehicle):
    def __init__(self, name : str, brand : str, color : str,capacity:str,plate_number:str,bus_name:str) -> None:
        super().__init__(name, brand, color,capacity,plate_number)
        self.bus_name=bus_name

    def drive(self):
        return f"the {self.bus_name}  is driving!"
    def drift(self):
        return f"the {self.bus_name} is not drifting !!"
    
    def carry_cargo(self):
        return f"the {self.bus_name} is carrying cargo !!"

class truck(Vehicle):
    def __init__(self, name : str, brand : str, color : str,capacity:str,plate_number:str,truck_name:str) -> None:
        super().__init__(name, brand, color,capacity,plate_number)
        self.truck_name=truck_name
    def drive(self):
        return f"the {self.truck_name}  is driving!"
    def drift(self):
        return f"the {self.truck_name} is not drifting !!"
    
    def carry_cargo(self):
        return f"the {self.truck_name} is not carrying cargo !!"


Vehicle1=Vehicle("corvett","chevrolet","red","4","12w34")
bus1=bus("microbus","nissan","white","10","00q9","Shuttle bus")
truck1=truck("trucktor","cat","black","2","6tte2"," buildozer")

print(Vehicle1.drive())
print(Vehicle1.drift())
print(Vehicle1.carry_cargo())

print(bus1.drive())
print(bus1.drift())
print(bus1.carry_cargo())

print(truck1.drive())
print(truck1.drift())
print(truck1.carry_cargo())