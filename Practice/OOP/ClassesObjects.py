# Create a Class
class MyClass:
    x = 5


print(MyClass)


# Create Object
class MyClass:
    x = 5


p1 = MyClass()
print(p1.x)


# The __init__() Function:
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties,
# or other operations that are necessary to do when the object is being created.
# The __init__() function is called automatically every time the class is being used to create a new object.
class Person:
    b = 6  # class variable

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("Shihab", 24)  # Instance

print(p1.name)
print(p1.age)
print(Person.b)
print(p1.b)
print(p1.__dict__)


# Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("Shihab", 24)
p1.myfunc()


# The self Parameter:
# The self parameter is a reference to the current instance of the class,
# and is used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like,
# but it has to be the first parameter of any function in the class.
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)


p1 = Person("Shihab", 24)
p1.myfunc()


# Modify Object Properties:
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)


p1 = Person("Shihab", 24)
p1.age = 22
print(p1.age)
print(hasattr(p1, "age"))  # check if an attribute exists or not.
print(getattr(p1, "age"))  # access the attribute of object.
# setattr(obj,name,value) − to set an attribute. If attribute does not exist, then it would be created.
# delattr(obj, name) − to delete an attribute.


# Delete Object Properties
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)


p1 = Person("Shihab", 24)
del p1.age  # delete properties on objects by using the del keyword
# print(p1.age)  # create error. coz property of age of p1 object is deleted


# Delete Objects
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)


p1 = Person("Shihab", 24)
del p1  # delete objects by using the del keyword
# print(p1)  # create error. coz object p1 is deleted


# The pass Statement
# class definitions cannot be empty.
# but if for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
class Person:
    pass


# Built-In Class Attributes:
# Every Python class keeps following built-in attributes and they can be accessed using dot operator.
"""
__dict__ − Dictionary containing the class's namespace.
__doc__ − Class documentation string or none, if undefined.
__name__ − Class name.
__module__ − Module name in which the class is defined. This attribute is "__main__" in interactive mode.
__bases__ − A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.
"""


class Employee:
    # Common base class for all employees
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displaycount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayemployee(self):
        print("Name : ", self.name, " , Salary : ", self.salary)


print("Employee.__doc__ : ", Employee.__doc__)
print("Employee.__name__ : ", Employee.__name__)
print("Employee.__module__ : ", Employee.__module__)
print("Employee.__bases__ : ", Employee.__bases__)
print("Employee.__dict__ : ", Employee.__dict__)


class Employees:

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    @classmethod
    def from_str(cls, string):
        # params = string.split("-")
        # print(params)
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))

    @staticmethod
    def good(string):
        print("Hello", string)


karan = Employees.from_str("Karan-580-Instructor")
print(karan.salary)
print(karan.good("Shihab"))
karan.good("Shihab")
