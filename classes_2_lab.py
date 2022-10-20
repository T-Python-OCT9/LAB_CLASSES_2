
class Vehicle:
    def __init__(self, brand : str, name : str, color : str, capacity:int, plate_number: str) -> None:
        #initilizing the class
        #instance attributes / properties
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number
        #private instance attribute

       #definig a setter for the private attribute
    def setBrand(self, brand : str):
        if len(brand) > 3 :
          self.__brand = brand

    def setName(self, name : str):
        if len(name) >2 :
          self.__name = name

    def setColor(self, color : str):
        if color == "black":
            print("please change the color")
        else:  self.__color = color

    def setcapacity(self, capacity : int):
        if capacity > 9:
          self.__capacity = capacity

    def setPlate_number(self, plate_number : str):
        if len(plate_number) == 4:
            self.__plate_number = plate_number
    

    #define a getter for the private attribute
    def getBrand(self):
        return self.__brand

    def getColor(self):
        return self.__color

    def getCapacity(self):
        return self.__capacity

    def getName(self):
        return self.__name
    
    def getPlate_number(self):
        return self.__plate_number
       
        

    def drive(self):
        print(f"the {self.name} is driving!")
    
    def drift(self):
        print(f"the is {self.name} drifting !!")
        
    def carry_cargo(self):
        print(f"the {self.name} is carrying cargo !!") 

   
# override
class Bus(Vehicle):
    
  def drive(self):
    print ("The override has been done successfully ")

class Truck(Vehicle):
    pass


# create objects
object_One= Vehicle ("KIA","ffffff","blue",4,"hhlm")
object_Two= Bus ("KIA","ffffff","blue",4,"hhlm")
Object_Three = Truck

print(object_One.drift())
print(object_Two.drive())
