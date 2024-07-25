from abc import ABC, abstractmethod

# An abstract class can be considered as a blueprint for other classes.
# It allows you to create a set of methods that must be created within any child classes built from the
# abstract class.
# By defining an abstract base class, can define a common Application Program Interface(API) for a set of subclasses.
# We cannot create object of Abstract Base Class.


class Polygon(ABC):
    # abstract method
    @abstractmethod
    def noofsides(self):
        pass


class Triangle(Polygon):
    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")


class Pentagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")


class Hexagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 6 sides")


class Quadrilateral(Polygon):

    # overriding abstract method
    def noofsides(self):
        print("I have 4 sides")


# Driver code
R = Triangle()
R.noofsides()

K = Quadrilateral()
K.noofsides()

R = Pentagon()
R.noofsides()

K = Hexagon()
K.noofsides()
print()


# Implementation Through Subclassing :
class Parent:
    def geeks(self):
        pass


class Child(Parent):
    def geeks(self):
        print("Child class")


# Driver code
print(issubclass(Child, Parent))
print(isinstance(Child(), Parent))
