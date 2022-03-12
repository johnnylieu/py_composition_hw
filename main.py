class Honda:
    def __init__(self, model, make, owner):
        self.model = model
        self.make = make
        self.owner = owner
        print(f"the owner of this {self.model} {self.make} is {self.owner}")
    
    def horn(self):
        print(f"{self.model} {self.make} horn activated, beep beep")
    
    def gas(self):
        print(f"you stepped on {self.model} {self.make}'s gas, speed increasing")

    def brake(self):
        print(f"you stepped on {self.model} {self.make}'s brake, speed decreasing")


class Toyota:
    def __init__(self, model, make, owner):
        self.model = model
        self.make = make
        self.owner = owner
        print(f"the owner of this {self.model} {self.make} is {self.owner}")

    def horn(self):
        print(f"{self.model} {self.make} horn activated, beep beep")
    
    def gas(self):
        print(f"you stepped on {self.model} {self.make}'s gas, speed increasing")

    def brake(self):
        print(f"you stepped on {self.model} {self.make}'s brake, speed decreasing")

class Car:
    def __init__ (self, honda, toyota):
        self.honda = honda
        self.toyota = toyota

cars = Car(Honda("Honda", "Civic", "Somebody"), Toyota("Toyota", "Camry", "Somebody Else"))

cars.honda.horn()
cars.honda.gas()
cars.honda.brake()

cars.toyota.horn()
cars.toyota.gas()
cars.toyota.brake()

# Create classes for Honda Civic 2022, Toyota Camry 2021. 
# No inheritance. 
# They should support have properties like name, model, and make of the car, name of owner. 
# They should have a horn, gas, brake, and parking brake function.