class Car:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

class Dealership:
    def __init__(self, owner, year, make, model):
        self.owner = owner
        self.car = Car(year, make, model)

        print(f"I am a {self.car.year} {self.car.make} {self.car.model}. I am owned by {owner}.")

mercedes = Dealership("Johnny", "2023", "Mercedes", "Maybach S600 AMG")
tesla = Dealership("Tyler", "2023", "Tesla", "X")
beamer = Dealership("Jonathan", "2023", "BWM", "7 Series")


# Composition HW
# Car
#    Honda
#        Civic
#        Accord
#    Toyota
#        Camry