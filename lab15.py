class Vehicle:


    def __init__(self, brand, name, color, capacity, plate_number) -> None:

        self.brand = brand
        self.name = name
        self.color = color
        self.capacity = capacity
        self.plate_number = plate_number

    def drive(self):
        return f"the {self.name} is driving!"

    def drift(self):
        return f"the {self.name} is drifting !!"

    def carry_cargo(self):
        return f"the {self.name} is carrying cargo !!"

    
class Bus(Vehicle):

    def __init__(self, brand, name, color, capacity, plate_number, Model) -> None:  
        super().__init__(brand, name, color, capacity, plate_number) 
        
    def drive(self):
        return f'when i was studing at School i used to take {self.brand}'

class Truck(Vehicle):
    
    def __init__(self, brand, name, color, capacity, plate_number, Model) -> None:  
        super().__init__(brand, name, color, capacity, plate_number)
        
    def drive(self):

        return f'I like Amirecan {self.brand}'





car_1 = Vehicle('Tyota', 'Ahmed', 'White', '12', '1499')

car_2 = Vehicle('Lixes', 'marwan', 'Black', '2', '3455')

car_3 = Vehicle('Honda', 'yasser', 'Blue', '5', '4955')


print(car_1.drive())

print(car_2.drift())

print(car_3.carry_cargo())

Bus1 = Bus('GMC', 'aqeel', 'Yellow', '16', '7765', '2011')

Truck1 = Truck('Honda', 'abdullah', 'Gray', '2', '8555','2019')

print(Bus1.drive())

