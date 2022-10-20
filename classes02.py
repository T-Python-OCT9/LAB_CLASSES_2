#definig a class
class Vehicle:
    #class attribute
    type = "object"

    def __init__(self,brand:str,name:str,color:str,capacity:str,plate_number:int):
        #initilizing the class
        #instance attributes 
        self.brand = brand
        self.name = name 
        self.color = color
        self.capacity = capacity
        self.plate_number = plate_number

    #create motheds for the Vehicle
    def drive(self):
        return f"The {self.name},{self.brand} is driving !"

    def drift(self):
        return f"The {self.name},{self.brand} is drifting !!"

    def carry_cargo(self):
        return f"The {self.name},{self.brand} is carrying cargo!!"  


    #setter for the private attribute for name of the Vehicle
    def SetDrive(self,name:str):
        self.name= name
    def SetDrive(self,brand):
        self.brand=brand
    def SetDrive(self,color:str):
        self.color=color
    def SetDrive(self,capacity:str):
        self.capacity=capacity
    def SetDrive(self,plate_number:str):
        self.plate_number= plate_number

    # getter for the private attriubte for name of the Vehicle
    def getDrive(self,plate_number):
        return f'The plate number is: {self.plate_number}'
    def getDrive(self,name):
        return f'The name of the vehicle is: {self.name}'
    def getDrive(self,brand):
        return f'The vehicle brand is: {self.brand}'
    def getDrive(self,capacity):
        return f'The vehicle capacity is: {self.capacity}'
    def getDrive(self,color):
        return f'The vehicle color is: {self.color}'


    #inheritance Bus class
class Bus(Vehicle):
    def __init__(self, brand, name, color, capacity, plate_number,passengers):
        super().__init__(brand, name, color, capacity, plate_number)
        self.passengers = passengers
     
    
   

    #setter the passenger attriubtte
    def SetPassengers (self,passengers):

        self.passengers= passengers
    #getter for the passengers attriubttee    
    def Getcargo(self,passenger):
        return self.passenger  

    def drive(self):
        print(f"The bus name is {self.name},and the brand {self.brand} can take {self.capacity} passenger ")

    def drift(self):
        print(f"the {self.name} doesn't drift !!")

#inheritance for Truck class
class Truck(Vehicle):
    def __init__(self, brand, name, color, capacity, plate_number,cargo):
        super().__init__(brand, name, color, capacity, plate_number)
        self.cargo= cargo

    #setter the cargo attriubtte
    def SetCargo (self,cargo):
        self.cargo= cargo
    #getter for the cargo attriubttee 
    def Getcargo(self,cargo):
        return self,cargo    

    def drift(self):
        print(f"the {self.name}and brand {self.brand} does drift !!") 

Vehicle1=Vehicle("BMW", "Mazda", "Black","5", "KYS 1433")  

Vehicle1.drive()
print(Vehicle1.SetDrive("KYS 1433"))

Bus1=Bus("Mercedes-Benz Citaro", "Single Decker Bus", "blue","20-30", "HIT 5345","Students")
Bus1.drive()
Bus1.SetPassengers("Students")
Bus1.drift()

Truck1=Truck("volvo","shipments Truck", "white", "10-140 shipments", "SKB 8686","Shipments")
Truck1.carry_cargo()
Truck1.SetCargo("Shipments")
Truck1.carry_cargo()
