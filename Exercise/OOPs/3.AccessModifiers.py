# All the class variables are public. Public variables can be accessed and modified from anywhere.
class Car:
    def __init__(self, window, door, engine_type):
        self.windows = window
        self.doors = door
        self.engine_type = engine_type


car = Car(4, 4, 'Diesel')
print(car)
print(dir(car))
car.windows = 6
print(car.windows)


# All the class variables are protected. The variables are only accessible and can be overridden from subclass.
class Vehicle:
    def __init__(self, window, door, engine_type):
        self._windows = window
        self._doors = door
        self._engine_type = engine_type


car1 = Vehicle(4, 4, 'Diesel')
print(car1)
print(dir(car1))


class Bus(Vehicle):
    def __init__(self, window, door, engine_type, vehicle_type):
        super(Bus, self).__init__(window, door, engine_type)
        self.vehicle_type = vehicle_type


bus = Bus(16, 2, 'Diesel', 'Manual')
print(dir(bus))
bus._doors = 1
print(bus._doors)


# private access modifiers are accessible within the class only, can not be accessed and modified outside of the class.
class Car:
    def __init__(self, window, door, engine_type):
        self.__windows = window
        self.__doors = door
        self.__engine_type = engine_type


audi = Car(2, 3, 'Petrol')
print(audi)
print(dir(audi))
print(audi._Car__engine_type)
