# Proper Approach to create a class
# The method __init__ simulates the constructor of the class. This method is called when the class is instantiated.
class Vehicle:
    def __init__(self, vehicle_type, window, door, engine_type):
        self.vehicle = vehicle_type
        self.windows = window
        self.doors = door
        self.engine_type = engine_type

    def self_driving(self):
        return "Vehicle Engine type is {}".format(self.engine_type)


print(dir(Vehicle))
vehicle = Vehicle('Car', 4, 4, 'Petrol')
print(vehicle)
print(vehicle.__dict__)
print(vehicle.vehicle)
print(vehicle.self_driving())


# Bad Approach to create a class
class Car:
    pass


car1 = Car()
car1.windows = 5
car1.doors = 4
print()
print(car1.windows)

car2 = Car()
car2.windows = 3
car2.doors = 2
print(car2.windows)
car2.engine_type = 'Petrol'
print(car2.engine_type)
print(car2.__dict__)
