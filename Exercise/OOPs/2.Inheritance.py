# All the class variables are public
class Car:
    def __init__(self, window, door, engine_type):
        self.windows = window
        self.doors = door
        self.engine_type = engine_type

    def driving(self):
        print("Manual driving car")
        # return "Manual driving car"


car = Car(4, 4, 'Petrol')
print(car.windows)
car.driving()
# print(car.driving())
print(dir(car))


class Audi(Car):
    def __init__(self, window, door, engine_type, enable_ai):
        super(Audi, self).__init__(window, door, engine_type)
        # super().__init__(window, door, engine_type)
        self.enable_ai = enable_ai

    def self_driving(self):
        print("Audi supports SELF driving")


audi = Audi(4, 4, 'Diesel', True)
print(audi.doors)
print(audi.enable_ai)
audi.self_driving()
audi.driving()
print(dir(audi))
