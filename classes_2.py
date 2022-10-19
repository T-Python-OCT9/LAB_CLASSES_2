
from unicodedata import name


class Vehicle:
    def __init__(self, brand:str,name:str, color:str, capacity: float,plate_number:int) -> None:
        self.__brand= brand
        self.__name=name
        self.__color=color
        self.__capacity=capacity
        self.__plate_number=plate_number


    #set for all values

    def setBrand(self,brand:str):
        self.__brand=brand

    def setName(self,name:str):
        self.__name=name

    def setColor(self,color:str):
        self.__color=color
    
    def setCapacity(self,capacity:float):
        self.__capacity=capacity

    def setPlateNumber(self,plate_number:int):
        self.__plate_number=plate_number

    #get for all values

    def getBrand(self):
        return self.__brand

    def getName(self):
        return self.__name


    def getColor(self):
        return self.__color
    
    def getCapacity(self):
        return self.__capacity

    def getPlateNumber(self):
        return self.__plate_number
    
    #__________________________________________________________

    #method drive 
    def drive(self):
        return f"the {self.getName()} is driving!"
    
    #method drifting 

    def drift(self):
        return f"the {self.getColor()}{self.getName()} is drifting"

    #method caring

    def carry_cargo(self):
        return f"the {self.getName()} is carrying cargo with capacity {self.getCapacity()}"



#___________________________________________________________

#new class inherit from vehicle 

class Bus(Vehicle):

    def __init__(self, brand:str,name:str, color:str, capacity: float,plate_number:int, size:int) -> None:
        super().__init__(brand,name,color,capacity,plate_number)
        self.__size=size

    
    #set for size 
    def setSize(self,size:int):
        self.__size=size

    #git for size
    def getSize(self):
        return self.__size
    
    #override method
    def drive(self):
        return f"the {self.getName()} is driving very good! and it is for {self.getSize()} people"


#______________________________________________________________



#new class inherit from vehicle 
    
class Truck(Vehicle):

    def __init__(self, brand:str,name:str, color:str, capacity: float,plate_number:int, weight:float) -> None:
        super().__init__(brand,name,color,capacity,plate_number)
        self.__weight=weight


    #set for weight
    def setWeight(self,weight:float):
        self.__weight=weight
    
    #get for weight 
    def getWeight(self):
        return self.__weight

    #override method
    def carry_cargo(self):
        return f"the {self.getName()} is carrying cargo with capacity {self.getCapacity()}, it is carrying {self.getWeight()} ton"



#________________________________________________________________

#step 1 

#main class 
#creat object for vehicle class
vehicle1=Vehicle("any brand","car","black",36.8,1110) 
#creat object for bus class
bus1=Bus("any brand","bus","white",40.3,1320,30) 
#creat object for truck class
truck1=Truck("any brand","truck","red",60.8,1190,39.5)





#step 2 


#print frome class vehicle 

#print drive method for class vehicle
print("The call method drive from parents class :\n",vehicle1.drive())

print("")#for space
#print drift method for class vehicle
print("The call method drift from parents class :\n",vehicle1.drift())

print("")#for space
#print carry cargo method for class vehicle
print("The call method carry cargo from parents class :\n",vehicle1.carry_cargo())
print("-"*20)

#print from class bus
print("The call method drive that override on it from subclass:\n",bus1.drive())
print("-"*20)

#print frome class truck
print("The call method carry cargo that override on it from subclass:\n",truck1.carry_cargo(),"\n")


    
