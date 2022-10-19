from turtle import color


class Vehicle :
    kind = "car"
    
    brand = "BMW"
    name = "fahad"
    color = "blak"
    capacity = " "
    plate_number = "ABC234"

    def __init__(self,brand : str, name : str, color : str, capacity : int, plate_number : str) -> None:
        #private instance attribute
        self.brand = brand
        self.name = name
        self.color = color
        self.capacity = capacity
        self.plate_number = plate_number


    def set_brand(self,brand):
        self.__brand = brand
    def get_brand(self):
         return self.__brand   

    def set_name(self,name):
        self.__name = name
    def get_name(self):
         return self.__name  

    def set_color(self,color):
        self.__color = color
    def get_color(self):
         return self.__color 

    def set_capacity(self,capacity):
        self.__capacity = capacity
    def get_capacity(self):
         return self.__capacity            

    def set_plate_number(self,plate_number):
        self.__plate_number = plate_number
    def get_plate_number(self):
         return self.__plate_number 


    def drive(self,name):
        print("name woner car is: ",self.name)

    def drift(self,name):
        print("the vehicle name is drifting: ",self.name) 

    def carry_cargo(self,name):
        print("the vehicle name is carrying cargo: ",self.name) 




class Bus(Vehicle):
    def __init__(self, brand: str, name: str, color: str, capacity: int, plate_number : str, national_id: str) -> None:
       super().__init__(brand,name,color, capacity, plate_number)
       self.national_id = national_id
       
    

    def drive(self):
        super().drive(self.national_id)
        return f"and national id: {self.national_id}"



class Truck(Vehicle) :
    def __init__(self, brand: str, name: str, color: str, capacity: int, plate_number : str) -> None:
       super().__init__(brand,name,color, capacity, plate_number)

    def drift(self):
        super().drift(self.plate_number)
        print("and plate number is: ",self.plate_number) 

    def carry_cargo(self):
        super().carry_cargo(self.capacity)
        print("capacity is: ",self.capacity)  


r = Vehicle("BMW","sara","white",5,"DJK875") 
print(r) 

x = Bus("BMW","nora","blak",5,"ABC234","12376543")
print(x.drive())

y = Truck("BMW","Ahmad","blak",5,"XCF346")
print(y.drift())

z = Truck("TOYOTA","mohamad","blak","400","SDF345")
print(z.carry_cargo())