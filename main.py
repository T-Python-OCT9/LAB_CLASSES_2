class Vehicle: #class

    def __init__(self,brand,name,color,capacity,plate_number) -> None:
        self.brand = brand
        self.name = name
        self.color = color
        self.capacity = capacity
        self.plate_number = plate_number

    def drive(self):
        print(f"The vehicle name is: {self.name} driving")

    def drift(self):
        print(f"The vehicle\"{self.name}\" drifting")

    def carry_cargo(self):
        print(f"The vehicle\"{self.name}\" is carrying cargo ")

 
    def setbrand(self, brand : str ):
        self.brand = brand

    def setname(self, name : str ):
        self.name = name    

    def setcolor(self, color : str ):
        self.color = color

    def setcapacity(self, capacity : str ):
        self.capacity = capacity 

    def setcapacity(self, capacity : str ):
        self.capacity = capacity

    def setplate_number(self, plate_number : str ):
        self.plate_number = plate_number
 
    def getbrand(self):
        return self.brand 

    def getname(self):
        return self.name

    def getcolor(self):
        return self.color

    def getcapacity(self):
        return self.capacity

    def getplate_number(self):
        return self.plate_number


#sub classes(1)(#inheritance)
class Bus(Vehicle):
    def __init__(self, brand, name, color, capacity, plate_number,passengers) -> None:
        super().__init__(brand, name, color, capacity, plate_number)
        self.passengers = passengers

    def setpassengers(self, passengers : str ):
        self.passengers = passengers

    def getpassengers(self):
        return self.passengers 

    def drive(self):
        print(f"The Bus name is: {self.name} driving for {self.passengers}")


#sub classes(2)(#inheritance)
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
        print(f"The Truck\"{self.name}\" drifting ")
    def carry_cargo(self):
        print(f"The Truck\"{self.name}\" is carrying {self.cargo} ")

#Class
Vehicle1 = Vehicle("Mercedes","EQE","Black",4,"ADF 345")
Vehicle2 = Vehicle("Toyota","Land Cruiser","White",7,"KJF 987")

Vehicle1.drive()
Vehicle2.drift()

#Sub classes(#inheritance)
bus_1 = Bus("Bus","GQ","White",25,"GFS 655","Student")
Truck_1 = Truck("Truck","YU","White",3,"PLH 764","Food")

bus_1.drive()
bus_1.setpassengers("Human")
bus_1.drive()


Truck_1.carry_cargo()
Truck_1.setcargo("Foodstuffs")
Truck_1.carry_cargo()