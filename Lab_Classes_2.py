'''
LAB_CLASSES_2
'''
#define a Vehicle class
class Vehicle:

    kind= "vehicle"
    #properties 
    def __init__(self, brand , name , color , capacity , plate_number) -> None:
        self.__brand = brand
        self.__name = name
        self.___color = color
        self.__capacity = capacity
        self.__plate_number = plate_number
    

    #methods
    def drive(self) -> str :
        print(f"{self.getName()} is driving !!")
    
    def drift(self) -> str :
        print(f" {self.getName()} is drifting !!")

    def carry_cargo(self) -> str :
        print(f" {self.getName()} is carrying cargo !!")

#------------------------ GETTER & SETTER -------------------------------------------   
    #for each of the properties
    # do a setter & getter (encabsulate the data).

    #1------Brand---------
    def getBrand(self):
        return self.__brand

    def setBrand(self , brand : str):
        if not (isinstance(brand , str)):
            raise ValueError("brand name must be string")
        self.__brand = brand
    #2------Name---------
    def getName(self):
        return self.__name

    def setNAme(self , name : str):
        if not (isinstance(name , str)):
            raise ValueError("vihcle name must be string")
        self.__name = name
    
    #3------Color---------
    def getColor(self):
        return self.___color

    def setColor(self , color : str):
        if not (isinstance(color , str)):
            raise ValueError("color name must be string")
        self.___color = color

    #4------Plate Number---------
    def getPlate(self):
        return self.__plate_number
        
    def setPlate(self , plate_number : str):
        if not (isinstance(plate_number , str) ):
            raise ValueError("plate number must be string")
        self.__plate_number = plate_number

    #5------Capacity---------
    def getCapacity(self):
        return self.__capacity
        
    def setCapacity(self , capacity : str):
        if not (isinstance(capacity , int) and capacity >= 50):
            raise ValueError("capacity  must be integer and equal or more than 50 ")
        self.__capacity = capacity

#-------------------------------------------------------------------
#Create tow other subclasses (inherit from vehicle):
class Bus(Vehicle):
    #override
    def drift(self) -> None :
        print(f"The Bus {self.getName()} cannot drift !! ")
    
    def carry_cargo(self) -> None :
        print(f"The Bus {self.getName()} cannot carry cargo !! ")

#-------------------------------------------------------------------
class Truck(Vehicle) : 
    #override
    def drift(self) -> None :
        print(f"The Truck {self.getName()} cannot drift !! ")

#-------------------------------------------------------------------

# create at least one object of each class.
Car1 = Vehicle("chevrolet", "Caprice" ,"Black" , 5 , "ABC 2345")
Bus1 = Bus("Mercedes", "C1" ,"white" , 32 , "RMI 2345"  )
Truck1 = Truck("Volvo" , "Truck" , "Gray" , 4 , "BVD 4567" )



#call all the methods on each object. 
print("-----------------------------------------")
Car1.drive()
Car1.drift()
Car1.carry_cargo()



print("-----------------------------------------")
#accessing the instance attributes
Bus1.drive()
Bus1.drift()
Bus1.carry_cargo()



print("-----------------------------------------")
Truck1.drive()
Truck1.drift()
Truck1.carry_cargo()
