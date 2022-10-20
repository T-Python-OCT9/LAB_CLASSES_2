'''


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
- override استخدم الميثود قي السوب واد=زيد عليها  the methods as needed for each subclass of vehicle. 
- create at least one object of each class.
- call all the methods on each object. 

'''

## define a Vehicle class . it has the following structure :

#### properties
# - bran
# - name
# - color
# - capacity
# - plate_number

class Vehicle :
    def __init__(self , bran , name , color , capacity , plate_number):
       self.__bran = bran 
       self.__name=name
       self.__color = color 
       self.__capacity = capacity 
       self.__plate_number = plate_number 
       
    #- drive()
    #prints "the vehicle_name is driving!"
    def drive (self):
        return f" { self.__name}is driving!"


    #drift()
    #prints "the vehicle_name is drifting !!" or something else depending on the class.
    def drift (self):
        return f"the color {self.__color} for {self.__name}"
    
    # carry_cargo()
    #prints "the vehicle_name is carrying cargo !!" or something else depending on the class 
    def carry_cargo( self):
        return f" the plate num for {self.__name} is {self.__plate_number} have box 1 & 10"
  
    ### for each of the properties do a setter & getter (encabsulate the data).
    def setbran(self , bran):
        self.__bran= bran

    def getbran (self ):
        return self.__bran

    def setname(self , name):
        self.__name= name

    def getname(self):
        return self.__name

    def setcolor(self , color ):
        self.__color = color

    def getcolor (self):
        return self.__color
    
    def setcapacity(self , capacity ):
        self.__capacity = capacity

    def getcapacity (self):
        return self.__capacity

    def setplate_number (self , plate_number ):
        self.__plate_number = plate_number

    def getplate_number (self):
        return self.__plate_number


### Create tow other subclasses (inherit from vehicle):
# Bus
# Truck
    
class Bus(Vehicle):

    def __init__(self, bran, name, color, capacity, plate_number , PathNUm_bus ):
        super().__init__(bran, name, color, capacity, plate_number)
        self.PathNUm_bus=PathNUm_bus
       

class Truck(Vehicle):
    def __init__(self, bran, name, color, capacity, plate_number , PathNUm_truck ):
        super().__init__(bran, name, color, capacity, plate_number)
        self.PathNUm_truck=PathNUm_truck


    

'''
### Note
- override استخدم الميثود قي السوب واد=زيد عليها  the methods as needed for each subclass of vehicle. 
- create at least one object of each class.
- call all the methods on each object. 

''' 
Vehi1= Vehicle("jeep ", "G1", "black ", "10", "DSQ 2256") 
print(Vehi1.getbran() , Vehi1.getname() , Vehi1.getcolor() , Vehi1.getcapacity(), Vehi1.getplate_number())
print("  ")
bus1= Bus("nissan" , "B20", "gray", "200", "ACU 4479", "Street 20 ")
print("bath for bus is ", bus1.PathNUm_bus)
print("  ")
truck1 =Truck("nissan", "T40", "white", "300", "SSD 5028", "street 89")
print("bath for bus istruck1",truck1.PathNUm_truck)
print("  ")

print(Vehi1.carry_cargo())
print(Vehi1.drift())

print("")

print(bus1.drift())
print(truck1.carry_cargo())









