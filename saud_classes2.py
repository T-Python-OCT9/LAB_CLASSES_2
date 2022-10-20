import mailbox


class Vehicle :

    def __init__(self, brand : str, name : str, color : str, capacity : str , plate_number : int) -> None:
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate = plate_number

    def driver(self):
        return f"the {self.__name} is driving !!"

    def drift(self):
        return f"the {self.__brand} is drifting !!"

    def carry_cargo(self):
        return f"the {self.__name} is carrying cargo !!"

    def thecolor(self):
        return f"the {self.__color} is nice"
    
    def thecapacity(self): 
        return f"the {self.__capacity} is good"
    
    def thepalte(self):
        return f"the {self.__plate} is  greta "


class Bus(Vehicle) :
    car1= Vehicle("jeep","h1","Blue","sa",1212)
    print(car1.drift())



class Truck(Vehicle) :
    car= Vehicle("mstbeshi","truck1","sopra","rfi8",4444)
    print(car.driver())


car = Vehicle("nisan","skyline","black","d1",1111)
bus = Bus     ("gmc","c1","wigte","ffff",1222)
tracck = Truck("vivo","c2","green","vfvf",2222)

print(car.drift())
print(car.driver())
print(car.thecapacity())
print(car.thecolor())
print(car.thepalte())

print(bus.drift())
print(bus.driver())
print(bus.carry_cargo())

print(tracck.drift())
print(tracck.driver())
print(tracck.carry_cargo())

