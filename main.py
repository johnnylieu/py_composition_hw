class Car:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

class Dealership:
    def __init__(self, owner, year, make, model):
        self.owner = owner
        self.car = Car(year, make, model)

    def speak(self):
        print(f"\n{self.owner} just bought our {self.car.year} {self.car.make} {self.car.model}.\n")


Johnny = Dealership("Johnny", "2023", "Mercedes", "Maybach S600 AMG").speak()
Tyler = Dealership("Tyler", "2023", "Tesla", "Model X").speak()
Jonathan = Dealership("Jonathan", "2023", "BWM", "6 Series").speak()


# Composition HW
# Car
#    Honda
#        Civic
#        Accord
#    Toyota
#        Camry