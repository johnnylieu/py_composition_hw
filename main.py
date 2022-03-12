class Honda:
    def __init__(self, model, make):
        self.model = model
        self.make = make

class Toyota:
    def __init__(self, model, make):
        self.model = model
        self.make = make

class Car:
    def __init__ (self, honda, toyota):
        self.honda = Honda
        self.toyota = Toyota


# Create classes for Honda Civic 2022, Toyota Camry 2021. 
# No inheritance. 
# They should support have properties like name, model, and make of the car, name of owner. 
# They should have a horn, gas, brake, and parking brake function.

# Show usgae of inheritance. Code duplication. Demonstrate DRY. Do it using inheritance.
# Car:
#   - HondaCivic
#   - ToyotaCamry

from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def gas():
        pass

    @abstractmethod
    def brake():
        pass

    def parking_brake(self):
        # Actual logic here
        print("parkingbrake")
        pass


class AcuraCivic(Car):
    NAME = "civic"

    def __init__(self, model, color, owner):
        self.model = model
        self.color = color
        self.owner = owner
        print(f"I'm a {color} Honda {HondaCivic.NAME} {model} owned by {owner}")

    def gas(self):
        pass

    def brake(self):
        pass


class AcuraAccord(Car):
    NAME = "accord"

    def __init__(self, model, color, owner):
        self.model = model
        self.color = color
        self.owner = owner
        print(f"I'm a {color} Honda {HondaCivic.NAME} {model} owned by {owner}")

    def gas(self):
        pass

    def brake(self):
        pass
    

class ToyotaCamry(Car):
    NAME = "camry"

    def __init__(self, model, color, owner):
        self.model = model
        self.color = color
        self.owner = owner
        print(f"I'm a {color} Toyota {ToyotaCamry.NAME} {model} owned by {owner}")

    def gas(self):
        pass

    def brake(self):
        pass


charlie = HondaCivic("2022", "black", "Tyler")
herbie = HondaCivic("2022", "grey", "Johnny")
tyler = HondaCivic("2022", "brown", "Jonathan")


charlie.parking_brake()


# print

# Honda.car = "four"

# print(Honda.car)

# print(honda_civic.car)
# Honda.NAME = "honda1"
# # honda_civic.NAME = "honda1"
# print(honda_civic.NAME)
# print(Honda.NAME)


class Vegetable():
    def __init__(self, color, ripeness):
        pass

class RGBColor():
    def _init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

class CLKColor():
    def __init__(color):
        selfcolor = color

class Ripeness():
    def _init__(self, ripeness):
        self.ripeness = ripeness
    
    def is_it_ready_to_eat(self):
        return False

rgb_color = RGBColor()
clk_color = CLKColor()
ripeness = Ripeness()

spinach = Vegetable(color=rgb_color, ripeness=ripeness)
kale = Vegetable(color=clk_color, ripeness=ripeness)


class Vegetable():
    pass


class RGBColorABCRipenessVegetable(Vegetable):
    pass


class CLKColorABCRipenessVegetable(Vegetable):
    pass


class RGBColorXYZRipenessVegetable(Vegetable):
    pass


class CLKColorXYZRipenessVegetable(Vegetable):
    pass