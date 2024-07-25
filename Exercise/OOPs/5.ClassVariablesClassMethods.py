class Car:
    base_price = 10000  # Class Variables

    def __init__(self, window, door, power):
        self.windows = window
        self.doors = door
        self.power = power

    def initial_price(self):
        print("Base price of the car is ${}".format(self.base_price))

    @classmethod
    def revise_initial_price(cls, inflation):
        cls.base_price = cls.base_price + cls.base_price * inflation


car1 = Car(4, 4, 2000)
print(car1.base_price)
print(Car.base_price)
print()

Car.revise_initial_price(0.10)
print(Car.base_price)
car2 = Car(4, 4, 2000)
print(car2.base_price)
print()

# Not a good practice to call the class method
car2.revise_initial_price(0.10)
print(car2.base_price)
print(car1.base_price)
print(Car.base_price)
