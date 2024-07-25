# Create a Parent Class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


x = Person("Shihab", "Ahmed")
x.printname()


# Create a Child Class
# send the parent class as a parameter when creating the child class
# Use the pass keyword when you do not want to add any other properties or methods to the class.
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):  # Now the Student class has the same properties and methods as the Person class.
    pass


x = Student("Mike", "Olsen")
x.printname()


# Add the __init__() Function
# We want to add the __init__() function to the child class (instead of the pass keyword)
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# The child's __init__() function overrides the inheritance of the parent's __init__() function.
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname):
        self.fn = fname
        self.ln = lname

    def pname(self):
        print(self.fn, self.ln)


x = Student("Mike", "Olsen")
x.pname()


# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


x = Student("Shihab", "Ahmed")
x.printname()

# Use the super() Function
# Python has a super() function that will make the child class inherit all the methods and properties from its parent.
# By using the super() function, you do not have to use the name of the parent element,
# it will automatically inherit the methods and properties from its parent.
print("\nSuper() function:")


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)


x = Student("Shihab", "Ahmed")
x.printname()


# Add Properties
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2020


x = Student("Shihab", "Ahmed")
print(x.graduationyear)


# Add a year parameter, and pass the correct year when creating objects
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year


x = Student("Shihab", "Ahmed", 2021)
print(x.graduationyear)


# Add Methods
# If you add a method in the child class with the same name as a function in the parent class, the inheritance of
# the parent method will be overridden.
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


x = Student("Mike", "Olsen", 2020)
x.welcome()
x.printname()


# Overriding Methods:
class Parent:        # define parent class
    def mymethod(self):
        print('Calling parent method')


class Child(Parent):  # define child class
    def mymethod(self):
        print('Calling child method')


c = Child()          # instance of child
c.mymethod()         # child calls overridden method
print()


# Real Life Example of method overriding:
class Bank:
    def getroi(self):
        return 10


class SBI(Bank):
    def getroi(self):
        return 7


class ICICI(Bank):
    def getroi(self):
        return 8


b1 = Bank()
b2 = SBI()
b3 = ICICI()
print("Bank Rate of interest:", b1.getroi())
print("SBI Rate of interest:", b2.getroi())
print("ICICI Rate of interest:", b3.getroi())
print()


# Overloading Operators:
# Dunder or magic methods in Python are the methods having two prefix and suffix underscores in the method name.
# Dunder here means “Double Under (Underscores)”
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)
print()


# Data abstraction(Hiding):
# An object's attributes may or may not be visible outside the class definition.
# attributes with a double underscore prefix, are not be directly visible to outsiders.
class JustCounter:
    __secretCount = 0  # double underscore prefix known as name mangling

    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
# print(counter.__secretCount)  # will rise an error.. coz variable is private
# You can access such attributes as object._className__attrName.
# print(counter._JustCounter__secretCount)
print()


class Employee:
    __count = 0

    def __init__(self):
        Employee.__count = Employee.__count+1

    def display(self):
        print("The number of employees", Employee.__count)


emp = Employee()
emp2 = Employee()
try:
    print(emp.__count)
except:
    print("AttributeError: 'Employee' object has no attribute '__count'")
finally:
    emp.display()
print()


# Python Multi-Level inheritance:
class Animal:
    def speak(self):
        print("Animal Speaking")


# The child class Dog inherits the base class Animal
class Dog(Animal):
    def bark(self):
        print("dog barking")


# The child class Dogchild inherits another child class Dog
class DogChild(Dog):
    def eat(self):
        print("Eating bread...")


d = DogChild()
d.bark()
d.speak()
d.eat()
print()


# Python Multiple inheritance:
class Calculation1:
    def Summation(self, a, b):
        return a+b


class Calculation2:
    def Multiplication(self, a, b):
        return a*b


class Derived(Calculation1, Calculation2):
    def Divide(self, a, b):
        return a/b


d = Derived()
print(d.Summation(10, 20))
print(d.Multiplication(10, 20))
print(d.Divide(10, 20))
print()


# The issubclass(sub,sup) method:
# The issubclass(sub, sup) method is used to check the relationships between the specified classes.
# It returns true if the first class is the subclass of the second class, and false otherwise.
class Calculation1:
    def Summation(self, a, b):
        return a+b


class Calculation2:
    def Multiplication(self, a, b):
        return a*b


class Derived(Calculation1, Calculation2):
    def Divide(self, a, b):
        return a/b


d = Derived()
print(issubclass(Derived, Calculation2))
print(issubclass(Calculation1, Calculation2))
print()


# The isinstance (obj, class) method:
# The isinstance() method is used to check the relationship between the objects and classes.
# It returns true if the first parameter, i.e., obj is the instance of the second parameter, i.e., class.
class Calculation1:
    def Summation(self, a, b):
        return a+b


class Calculation2:
    def Multiplication(self, a, b):
        return a*b


class Derived(Calculation1, Calculation2):
    def Divide(self, a, b):
        return a/b


d = Derived()
print(isinstance(d, Derived))

# Dunder methods(Double Underscore Methods) or Magic Functions:
a = 7
print(a.__mul__(6))


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        return self.salary + other.salary

    def __repr__(self):
        return 'Employee({}, {})'.format(self.name, self.salary)

    def __str__(self):
        return "Employee name is {}".format(self.name)


s = Employee("Shihab", 9600)
a = Employee("Ahmed", 9600)
print(s+a)
print(repr(s))
print(str(s))
print(s)
