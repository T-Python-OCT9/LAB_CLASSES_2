'''

# LAB_CLASSES_2

## define a Vehicle class . it has the following structure :

#### properties
- brand
- name
- color
- capacity
- plate_number


#### methods
- drive()
  prints "the vehicle_name is driving!"
- drift()
  prints "the vehicle_name is drifting !!" or something else depending on the class.
- carry_cargo()
  prints "the vehicle_name is carrying cargo !!" or something else depending on the class


### for each of the properties do a setter & getter (encabsulate the data).

### Create tow other subclasses (inherit from vehicle):
- Bus
- Truck


### Note
- override the methods as needed for each subclass of vehicle. 
- create at least one object of each class.
- call all the methods on each object. 

'''


class Vehicle :


  def __init__(self, brand : str, name : str, color : str , capacity : int , plate_number : int) -> None:

         self.__brand = brand
         self.__name = name
         self.__color = color 
         self.__capacity = capacity
         self.__plate_number = plate_number




  def setbrand (self, brand : str):
        if not (isinstance(brand, str)):
             raise ValueError("string type")
        self.__brand = brand

  def getbrand(self):
         return self.__brand



  def setname (self, name : str):
        if not (isinstance(name, str)):
             raise ValueError("string type")
        self.__name = name

  def getname(self):
         return self.__name



  def setcolor (self, color : str):
        if not (isinstance(color, str)):
             raise ValueError("string type")
        self.__color = color


  def getcolor(self):
         return self.__color


  def setcapacity (self, capacity : int):
        if not (isinstance(capacity, int)):
             raise ValueError("integer type")
        self.__capacity = capacity

  def getcapacity(self):
         return self.__capacity


  def setplate_number (self, plate_number : int):
        if not (isinstance(plate_number, int) and len(plate_number) == 4):
             raise ValueError("4 numbers")
        self.__plate_number = plate_number

  def getplate_number(self):
         return self.__plate_number


  def drive(self):
     print(f"The {self.__name } is driving!")


  def drift(self):
     print(f"The {self.__name} is drifting!")


  def carry_cargo(self):
    print(f"The {self.__name} is carrying cargo!")

 
    

Vehicle1 = Vehicle ("mercedes", "maybach", "black", 4, "HAC 1")

    
    
    
class Bus(Vehicle):
     def carryCargo(self):
         print(f"The bus is a {self.getbrand()}, brand  and can carry about {self.getcapacity()}")

     def drive(self):
         print(f"The bus: {self.getName()} is driving")
         
         
    
         
class Truck(Vehicle):
     def carryCargo(self):
         print(f"The truck is a {self.getbrand()}, brand  and can carry about {self.getcapacity()}")

     def drive(self):
         print(f"The truck: {self.getName()} is driving")

Bus1 = Bus("Lexus", "lexus lx 570", "navy blue", "6", "RAZ 22")
Truck1 = Truck("Audi", "Audi Q8", "grey", "4", "ABC 1234")


Bus1.drive()
Bus1.drift()
Bus1.carryCargo()
Truck1.drive()
Truck1.drift()
Truck1.carryCargo()