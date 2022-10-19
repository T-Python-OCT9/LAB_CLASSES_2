#this is classes lab 2 - oct 19 - ghadah alahrbi 
class Vehicle:

    def __init__(self ,brand : str , name :str ,color: str ,capacity: int, plate_number:str ) :
        self.__brand=brand
        self.__name=name
        self.__color=color 
        self.__capacity=capacity
        self.__plate_number=plate_number

#setter and getter for each attribute 
    def setbrand(self , brand ):
        self.__brand=brand
    
    def getbrand(self ):
        return self.__brand
    
    def setname(self , name):
        self.__name=name 
    
    def getname(self):
        return self.__name
    
    def setcolor(self , color):
        self.__color=color

    def getcolor(self):
       return  self.__color 
    
    def setcap(self, cap):
        self.__capacity=cap 
    
    def getcap(self):
        return self.__capacity

    def setplatenum(self , platen):
        self.__plate_number=platen

    def setplatenum(self):
        return self.__plate_number

#creating methodes

    def drive(self) :
        print(f"this methode from main class ,the {self.getname()} is driving!")
    
    def drift(self):
        print(f"this methode from main class ,the {self.getname()} is drifting !!")
    
    def carry_cargo(self):
        print(f"this methode from main class ,the {self.getname()} is carrying cargo !!")


    

class bus(Vehicle):

    def __init__(self, brand: str, name: str, color: str, capacity: int, plate_number: str):
        super().__init__(brand, name, color, capacity, plate_number)
     
    def drift(self ):
        print(f"this methode is from bus class (override ), the {self.getname()} is drifting !!")




class Truck(Vehicle):
    def __init__(self, brand: str, name: str, color: str, capacity: int, plate_number: str):
        super().__init__(brand, name, color, capacity, plate_number)
    
    def carry_cargo(self ):
        print(f"this methode is from truck class (override ),the {self.getname()} is carrying cargo !!")


#creating objects from each class 
v= Vehicle("Toyota", "Toyota RAV4","red", 6 ,"uiu888")
b=bus("Jelcz", "Jelcz 021" ,"green",30,"oioi999")
t=Truck("Kenworth", "kenname","blue",40,"iii090")

v.drive()
v.drift()
v.carry_cargo()


b.drive()
b.drift()
b.carry_cargo()

t.drive()
t.drift()
t.carry_cargo()