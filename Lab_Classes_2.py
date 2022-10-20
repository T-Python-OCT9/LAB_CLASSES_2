'''
LAB_CLASSES_2
'''
#define a Vehicle class
class Vehicle:

    kind= "vehicle"
    #properties 
    def __init__(self, brand , name , color , capacity , plate_number) -> None:
        self._brand = brand
        self._name = name
        self._color = color
        self._capacity = capacity
        self._plate_number = plate_number
    

    #methods
    def drive(self) -> str :
        print(f"{self._name} is driving  {self._brand}")
    
    def drift(self) -> str :
        print(f" {self._name} is drifting !!")

    def carry_cargo(self) -> str :
        print(f" {self._name} is carrying cargo !!")

#------------------------ GETTER & SETTER -------------------------------------------   
    #for each of the properties
    # do a setter & getter (encabsulate the data).

    #1------Brand---------
    def getBrand(self):
        return self._brand

    def setBrand(self , brand : str):
        if not (isinstance(brand , str)):
            raise ValueError("brand name must be string")
        self._brand = brand
    #2------Name---------
    def getName(self):
        return self._name

    def setNAme(self , name : str):
        if not (isinstance(name , str)):
            raise ValueError("vihcle name must be string")
        self._name = name
    
    #3------Color---------
    def getColor(self):
        return self._brand

    def setColor(self , color : str):
        if not (isinstance(color , str)):
            raise ValueError("color name must be string")
        self._color = color

    #4------Plate Number---------
    def getPlate(self):
        return self._plate_number
        
    def setPlate(self , plate_number : str):
        if not (isinstance(plate_number , int) and len(str(plate_number)) == 4):
            raise ValueError("plate number must be integer and equal to 4")
        self._plate_number = plate_number

    #5------Capacity---------
    def getCapacity(self):
        return self._capacity
        
    def setCapacity(self , capacity : str):
        if not (isinstance(capacity , int) and capacity >= 50):
            raise ValueError("capacity  must be integer and equal or more than 50 ")
        self._capacity = capacity

#-------------------------------------------------------------------
#Create tow other subclasses (inherit from vehicle):
class Bus(Vehicle):

    def __init__(self, brand, name, color, capacity, plate_number , ticket_price) -> None:
        super().__init__(brand, name, color, capacity, plate_number)
        self.ticket_price = ticket_price

    def BusDetails(self):
        return f"The Bus name is : {self._name} | color is : {self._color} , and the ticket price is {self.ticket_price}"

    #override
    def drive(self) -> str :
        print(f" {self._name} type is bus  , brand : {self._brand}   ")

#-------------------------------------------------------------------
class Truck(Vehicle) : 

    def __init__(self, brand, name, color, capacity, plate_number , path) -> None:
        super().__init__(brand, name, color, capacity, plate_number)
        self.path = path

    def TruckDetails(self):
        return f"The Truck name is : {self._name} capacity is : {self._capacity} , and it has a private path called : {self.path} "

    #override
    def carry_cargo(self) -> str :
        print(f" {self._name} is carrying cargo !! , and it is a truck with color {self._color}")

# create at least one object of each class.
Car1 = Vehicle("BMW", "Car" ,"Black" , "5" , 2345)
Bus1 = Bus("Mercedes", "Bus" ,"white" , "15" , 2345 , 20)
Truck1 = Truck("Volvo" , "Truck" , "Gray" , "3" , 4567 ,"Truck Path")



#call all the methods on each object. 
print("-----------------------------------------")
#accessing the instance attributes
print(f"Vehicle brand: {Car1._brand} | Vehicle name : {Car1._name} | Color:  {Car1._color} | Capacity : {Car1._capacity} | Palte Number: {Car1._plate_number}")
Car1.drive()
Car1.drift()
Car1.carry_cargo()
Car1.setNAme("New Car")
print(Car1.getName())
#after modify car name
Car1.drive()

# print(Car1._name)
# print(Car1.drive())
# print(Car1.drift())
# print(Car1.carry_cargo())
# Car1.setNAme("New CAR")
# print(Car1.getName())
# Car1.setBrand("Some Brand")
# print(Car1.getBrand())
# Car1.setPlate(4673)
# print(Car1.getPlate())
# Car1.setCapacity(60)
# print(Car1.getCapacity())

print("-----------------------------------------")
#accessing the instance attributes
print(f"Vehicle brand: {Bus1._brand} | Vehicle name : {Bus1._name} | Color:  {Bus1._color} | Capacity : {Bus1._capacity} | Palte Number: {Bus1._plate_number}")
Bus1.drive()
Bus1.drift()
Bus1.carry_cargo()
Bus1.setNAme("New Bus")
print(Bus1.getName())
#after modify car name
Bus1.drift()

Bus1.setCapacity(70)
print(Bus1.getCapacity())
print(Bus1.BusDetails())

# print(Bus1._name)
# print(Bus1.drive())
# print(Bus1.drift())
# print(Bus1.carry_cargo())
# Bus1.setBrand("Some Brand2")
# print(Bus1.getBrand())
# Bus1.setPlate(4673)
# print(Bus1.getPlate())


print("-----------------------------------------")
#accessing the instance attributes
print(f"Vehicle brand: {Truck1._brand} | Vehicle name : {Truck1._name} | Color:  {Truck1._color} | Capacity : {Truck1._capacity} | Palte Number: {Truck1._plate_number}")
Truck1.drive()
Truck1.drift()
Truck1.carry_cargo()
Truck1.setNAme("New truck")
print(Truck1.getName())
#after modify car name
Truck1.drift()

Truck1.setCapacity(90)
print(Truck1.getCapacity())
print(Truck1.TruckDetails())

# print(Truck1._name)
# print(Truck1.drive())
# print(Truck1.drift())
# print(Truck1.carry_cargo())
# Truck1.setBrand("Some Brand3")
# print(Truck1.getBrand())
# Truck1.setPlate(4642)
# print(Truck1.getPlate())
# Truck1.setCapacity(90)
# print(Truck1.getCapacity())
# print(Truck1.TruckDetails())