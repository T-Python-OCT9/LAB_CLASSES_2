
class Vehicle:
    def __init__(self, brand, name, color, capacity, plate_number) -> None:
        self.brand = brand
        self.name =  name
        self.color = color
        self.capacity = capacity
        self.plate_number = plate_number

    def drive(self):
        print(f"the {self.name} is driving!")

    def drift(self):
        if self.name == "gto 250":
            print(f"the {self.name} is drifting !!")
        else:
            print(f"{self.name} is not for drifting!")
    def carry_cargo(self):
        if self.name == "van":
            print(f"the {self.name} is carrying cargo !!")
        else:
            print(f"{self.name} is not for carrying!")

vehicle1 = Vehicle("ford", "torus", "black", 6, "hel 5000")
vehicle1.drive()
vehicle1.drift()
vehicle1.carry_cargo()

vehicle2 = Vehicle("ferarri", "gto 250", "red", 2, "Nar 0")
vehicle2.drive()
vehicle2.drift()
vehicle2.carry_cargo()

vehicle3 = Vehicle("toyota", "van", "White", 8, "jdi 2665")
vehicle3.drive()
vehicle3.drift()
vehicle3.carry_cargo()

