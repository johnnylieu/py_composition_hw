class Dealership:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

class Car:
    def __init__(self, owner, year, make, model):
        self.owner = owner
        self.dealership = Dealership(year, make, model)

        print(f"I am a {self.dealership.year} {self.dealership.make} {self.dealership.model} and I am owned by {self.owner}")


Mercedes = Car("Johnny", "2023", "Mercedes", "Maybach S600 AMG")


# Composition HW
# Car
#    Honda
#        Civic
#        Accord
#    Toyota
#        Camry