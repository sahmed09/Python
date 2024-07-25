import datetime

now = datetime.datetime.now()


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

    @staticmethod  # When the class is loaded, the first thing gets initialized is the static method
    def check_year():
        if now.year == 2024:
            return True
        else:
            return False


print(Car.check_year())

car1 = Car(4, 4, 2000)
print(car1.check_year())

if car1.check_year():
    pass
else:
    Car.revise_initial_price(0.10)

print(car1.base_price)
