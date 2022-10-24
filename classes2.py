class Vehicle:
    def __init__(self,brand,name,color,capacity,plate_number) -> None:
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number
    
    def drive(self):
        print(f"The vehicle name is: {self.getname()} driving")

    def drift(self):
        print(f"The vehicle\"{self.getname()}\" drifting !!")

    def carry_cargo(self):
        print(f"The vehicle\"{self.getname()}\" is carrying cargo !!")

    #setter------------
    def setbrand(self, brand : str ):
        self.__brand = brand
    
    def setname(self, name : str ):
        self.__name = name    

    def setcolor(self, color : str ):
        self.__color = color

    def setcapacity(self, capacity : str ):
        self.__capacity = capacity 

    def setcapacity(self, capacity : str ):
        self.__capacity = capacity

    def setplate_number(self, plate_number : str ):
        self.__plate_number = plate_number


    #getter-------------  
    def getbrand(self):
        return self.__brand 
    
    def getname(self):
        return self.__name
    
    def getcolor(self):
        return self.__color
    
    def getcapacity(self):
        return self.__capacity
     
    def getplate_number(self):
        return self.__plate_number
    


class Bus(Vehicle):
    def __init__(self, brand, name, color, capacity, plate_number,passengers) -> None:
        super().__init__(brand, name, color, capacity, plate_number)
        self.__passengers = passengers
    
    def setpassengers(self, passengers : str ):
        self.__passengers = passengers
  
    def getpassengers(self):
        return self.__passengers 

    def drive(self):
        print(f"The Bus name is: {self.getname()} driving for {self.getpassengers()}")





class Truck(Vehicle):
    def __init__(self, brand, name, color, capacity, plate_number, cargo) -> None:
        super().__init__(brand, name, color, capacity, plate_number)
        self.cargo = cargo
    
    def setcargo(self, cargo : str ):
        self.cargo = cargo
  
    def getcargo(self):
        return self.cargo

    def drive(self):
        print(f"The Truck name is: {self.name} driving")

    def drift(self):
        print(f"The Truck\"{self.getname()}\" drifting !!")

    def carry_cargo(self):
        print(f"The Truck\"{self.getname()}\" is carrying {self.getcargo()} !!")


Vehicle1 = Vehicle("BMW","Mazda","Black",5,"ASD 123")
Vehicle2 = Vehicle("Ford","Honda","White",4,"tyu 765")

Vehicle1.drive()
Vehicle2.drift()

bus1 = Bus("Bus","Ruza","White",16,"ghj 655","Student")
bus1.drive()
bus1.setpassengers("Employee")
bus1.drive()
Truck1 = Truck("Hino","Ranger","White",16,"hyt 987","Cars")
Truck1.carry_cargo()
Truck1.setcargo("Furniture")
Truck1.carry_cargo()
