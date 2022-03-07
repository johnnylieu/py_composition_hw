class Dealership:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

class Car:
    def __init__(self, owner, year, make, model):
        self.owner = owner
        self.car = Dealership(year, make, model)

    def speak(self):
        print(f"I am a {self.car.year} {self.car.make} {self.car.model}. I am owned by {self.owner}.")

Johnny = Car("Johnny", "2023", "Mercedes", "Maybach S600 AMG").speak()


# Composition HW
# Car
#    Honda
#        Civic
#        Accord
#    Toyota
#        Camry