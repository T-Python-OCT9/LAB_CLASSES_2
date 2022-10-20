class Vehicle:
### for each of the properties do a setter & getter (encabsulate the data).
    
    def __init__(self ,brand :str ,name:str, color:str , capacity:int , plate_number:int) -> None:
        self.brand = brand
        self.name = name
        self.color = color
        self.capacity = capacity
        self.plante_number = plate_number

    def drive(self):
        return f"the {self.name} is driving !"

    def drift(self):
         return f"the {self.name} is drifting !!" 

    def carry_cargo(self):
        return f"the {self.name} is carrying cargo !!"

    ##  Set ##
    def SetName(self, name :str):
        if not isinstance(name, str):
            raise ValueError("name must be String !")
        self.__name = name

    def SetBrand(self , brand:str):
        if not isinstance(brand, str):
            raise ValueError("brand must be String !")
        self.__brand = brand

    def SetColor(self , color:str):
        if not isinstance(color, str):
            raise ValueError("color must be String !")
        self.__color = color


    def SetCapacity(self , capacity:int):
        if not isinstance(capacity, int):
            raise ValueError("capacity must be integeer !")
        self.__capacity = capacity


    def SetPlate_number(self , plate_number:int):
        if not isinstance(plate_number,int):
            raise ValueError("plate_number must be integeer !")
        self.__plate_number = plate_number
    

     ##  Get ##
    def GetBrand(self):
        return self.__brand

    def GetName(self):
        return self.__name

    def GetColor(self):
        return self.__color

    def GetCapacity(self):
        return self.__capacity

    def GetPlate_number(self):
        return self.__plate_number


class Bus(Vehicle):
    def __init__(self, brand: str, name: str, color: str, capacity: int, plate_number: int , people_used:str , price:int) -> None:
        super().__init__(brand, name, color, capacity, plate_number)

        self.people_used = people_used
        self.price = price

    def introduceSelf(self):
        return f"the barand {self.brand} has a Bus {self.name} one of colors is {self.color},used for {self.people_used} and the price of car {self.price}"
    

    ## Set ##
    def SetPeople_used(self , people_used:str):
        if not isinstance(people_used,str):
            raise ValueError("people_used must be String !")
        self.__people_used = people_used


    def SetPrice(self , price:int):
        if not isinstance(price,int):
            raise ValueError("price must be integeer !")
        self.__price = price

     ##  Get ##
    def Getpeople_used(self):
        return self.__people_used

    def GetPrice(self):
        return self.__price



class Truck(Vehicle):
    def __init__(self, brand: str, name: str, color: str, capacity: int, plate_number: int ,used_TO:str , price:int) -> None:
        super().__init__(brand, name, color, capacity, plate_number)

        self.used_To = used_TO
        self.price = price

    def introduceSelf(self):
        return f"the barand {self.brand} has a truck {self.name} one of colors is {self.color},used for {self.used_To} and the price of car {self.price}"

     ## Set ##
    def SetUsed_To(self , used_To :str):
        if not isinstance(used_To ,str):
            raise ValueError("used_To must be String !")
        self.__used_To  = used_To 


    def SetPrice(self , price:int):
        if not isinstance(price,int):
            raise ValueError("price must be integeer !")
        self.__price = price

     ##  Get ##
    def GetUsed_To(self):
        return self.__used_To 

    def GetPrice(self):
        return self.__price



Vehicle1 = Vehicle("Audi" , "q8" , "black" , 1000 , 100)
print(Vehicle1.brand ,Vehicle1.name , Vehicle1.color , Vehicle1.capacity , Vehicle1.plante_number)

print(Vehicle1.drive())
print(Vehicle1.drift())
print(Vehicle1.carry_cargo())

Bus1 = Bus("Toyota" ,"Hiace" , "Black" ,100000 , 498 ,"Students" , 70.000)
print(Bus1.introduceSelf())

Truck1 = Truck("Toyota" ,"Tacoma" , "Blue" ,1000000 , 175 ,"Traking" , 167.382)
print(Truck1.introduceSelf())