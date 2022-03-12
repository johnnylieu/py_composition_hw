class Honda:
    def __init__(self, year, model, make, owner):
        self.year = year
        self.model = model
        self.make = make
        self.owner = owner
        print(f"The owner of this {self.year} {self.model} {self.make} is {self.owner}")
    
    def horn(self):
        print(f"{self.year} {self.model} {self.make} horn activated, beep beep")
    
    def gas(self):
        print(f"You stepped on {self.year} {self.model} {self.make}'s gas, speed increasing")

    def brake(self):
        print(f"You stepped on {self.year} {self.model} {self.make}'s brake, speed decreasing")


class Toyota:
    def __init__(self, year, model, make, owner):
        self.year = year
        self.model = model
        self.make = make
        self.owner = owner
        print(f"the owner of this {self.year} {self.model} {self.make} is {self.owner}")

    def horn(self):
        print(f"{self.year} {self.model} {self.make} horn activated, beep beep")
    
    def gas(self):
        print(f"You stepped on {self.year} {self.model} {self.make}'s gas, speed increasing")

    def brake(self):
        print(f"You stepped on {self.year} {self.model} {self.make}'s brake, speed decreasing")

class Car:
    def __init__ (self, honda, toyota):
        self.honda = honda
        self.toyota = toyota

cars = Car(Honda("2022", "Honda", "Civic", "Somebody"), Toyota("2021", "Toyota", "Camry", "Somebody Else"))

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