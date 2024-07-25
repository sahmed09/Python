from dataclasses import dataclass

"""Python Data Classes
In python, the dataclass decorator is a feature introduced in Python 3.7 that provides a concise way to define classes
primarily intended to store data. It automatically generates several special methods, such as init, repr, and eq,
based on the class attributes you define. This simplifies the process of creating and working with data-focused classes.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


print('General Form of Creating Class:')
person = Person('Shihab', 25)
print(person)
print(person.name)
print()

"""The @dataclass decorator automatically generates the following methods:
1. init(): Initializes the object and assigns the provided values of the attributes.
2. repr(): Provides a string representation of the object.
3. eq(): Implements quality comparison between two objects of the class based on their attributes."""


@dataclass
class Person:
    name: str
    age: int
    profession: str


print('Creating Class using Data Class:')
person1 = Person('Ahmed', 25, 'ML')
print(person1)
print(person1.name)


@dataclass
class Person:
    name: str
    age: int
    profession: str = 'AI'


person1 = Person('Ahmed', 25)
print(person1)
person1.profession = 'Data Analyst'
print(person1)
print()


# Immutable Class
@dataclass(frozen=True)  # when frozen=True, means we cannot change the attribute values
class Point:
    x: int
    y: int


print('Immutability Check:')
point = Point(3, 4)
print(point)
# point.x = 34  # Cannot assign new x value due to frozen=True
print()


# Inheritance
@dataclass
class Person:
    name: str
    age: int


@dataclass
class Employee(Person):
    employee_id: str
    department: str


print('Inheritance:')
person = Person('Shihab', 20)
print(person)

employee = Employee('Shihab', 20, '123', 'Programming')
print(employee)
print()


# Nested Data Class
@dataclass
class Address:
    street: str
    city: str
    zip: str


@dataclass
class Person:
    name: str
    age: str
    address: Address


print('Nested Data Class:')
address = Address('Main Street', 'Sylhet', '3100')
print(address)

person = Person('Ahmed', '23', address)
print(person)
print(person.address.street)
