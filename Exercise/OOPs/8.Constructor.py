# Python Constructor:
# A constructor is a special type of method (function) which is used to initialize the instance members of the class.
# Constructors can be of two types. Parameterized Constructor, Non-parameterized Constructor.

# Creating the constructor in python:
# the method __init__ simulates the constructor of the class. This method is called when the class is instantiated.
class Employee:
    def __init__(self, name, id):
        self.id = id
        self.name = name

    def display(self):
        print("ID: %d, Name: %s" % (self.id, self.name))


emp1 = Employee("John", 101)
emp2 = Employee("David", 102)
emp1.display()  # accessing display() method to print employee 1 information
emp2.display()  # accessing display() method to print employee 2 information
print()


"""Can We Have Multiple Constructors In Python?
Answer: No. We cannot have multiple constructors in python. The second constructor will override the first 
constructor.
Hack: It can be possible by using positional argument."""


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self, sound):
        return 'The animal is {} and says {}'.format(self.name, sound)


dog = Animal('Dog', 'Mammal', 6)
print(dog.age)
print(dog.make_sound('Woof Woof'))

"""Solution: Not a good practice"""


class Animal:
    def __init__(self, *args):
        if len(args) == 1:
            self.name = args[0]
        elif len(args) == 2:
            self.name = args[0]
            self.species = args[1]
        elif len(args) == 3:
            self.name = args[0]
            self.species = args[1]
            self.age = args[2]

    # def __init__(self, name, species, age):
    #     self.name = name
    #     self.species = species
    #     self.age = age

    def make_sound(self, sound):
        return 'The animal is {} and says {}'.format(self.name, sound)


dog = Animal('Dog', 'Mammal', 6)
print(dog.species)
