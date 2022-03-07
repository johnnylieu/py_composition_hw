class Car:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

class Dealership:
    def __init__(self, owner, year, make, model):
        self.owner = owner
        self.dealership = Dealership(year, make, model)

    def speak(self):
        print(f"I am a {self.dealership.year} {self.dealership.make} {self.dealership.model}. I am owned by {self.owner}.")

Johnny = Dealership("Johnny", "2023", "Mercedes", "Maybach S600 AMG").speak()


# Composition HW
# Car
#    Honda
#        Civic
#        Accord
#    Toyota
#        Camry