class Vehicle :


 def __init__(self, brand : str, name : str, color : str , capacity : int , plate_number : int) -> None:
      
        self.__brand = brand
        self.__name = name
        self.__color = color 
        self.__capacity = capacity
        self.__plate_number = plate_number
        



 def setbrand (self, brand : str):
       if not (isinstance(brand, str)):
            raise ValueError("the type should be string .")
       self.__brand = brand
    
 def getbrand(self):
        return self.__brand



 def setname (self, name : str):
       if not (isinstance(name, str)):
            raise ValueError("the type should be string .")
       self.__name = name
    
 def getname(self):
        return self.__name


              

 def setcolor (self, color : str):
       if not (isinstance(color, str)):
            raise ValueError("the type should be string .")
       self.__color = color
       
    
 def getcolor(self):
        return self.__color



 def setcapacity (self, capacity : int):
       if not (isinstance(capacity, int)):
            raise ValueError("the type should be integers .")
       self.__capacity = capacity
    
 def getcapacity(self):
        return self.__capacity


 def setplate_number (self, plate_number : int):
       if not (isinstance(plate_number, int) and len(plate_number) == 4):
            raise ValueError(" the plate number should be = 4 .")
       self.__plate_number = plate_number
    
 def getplate_number(self):
        return self.__plate_number
              
              
    
 def drive(self):
    print(f"The {self.__name } is driving!")


 def drift(self):
    print(f"The {self.__name} is drifting!")


 def carry_cargo(self):
   print(f"The {self.__name} is carrying cargo!")

v1 = Vehicle ("Mazda","cx30", "5" , "2222")




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

Bus1 = Bus('King long', '07', 'black', 50, 4444)
Truck1 = Truck('Volvo', 'x90', 'grey', 100, 1234)

Bus1.drive()
Bus1.drift()
Bus1.carryCargo()

Truck1.drive()
Truck1.drift()
Truck1.carryCargo()