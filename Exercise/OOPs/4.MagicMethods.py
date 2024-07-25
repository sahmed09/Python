# All the class variables are public
# Dunder Methods (Double Underscore Methods) or Magic Methods
class Car:
    # def __new__(self, window, door, engine_type):
    #     print("The object has started getting initialized")

    def __init__(self, window, door, engine_type):
        self.windows = window
        self.doors = door
        self.engine_type = engine_type

    def __str__(self):
        return "The object has been initialized"

    def __sizeof__(self):
        return "This displays size of the object"

    def driving(self):
        print("Manual driving car")


car = Car(4, 4, 'Petrol')
print(car)
car.driving()
print(dir(car))  # All (__**__) are magic methods.
print(car.__str__())
print(car.__sizeof__())

# Dunder Methods (Double Underscore Methods) or Magic Methods
a = 7
print(dir(a))
print(a.__mul__(6))
print(a.__divmod__(2))
