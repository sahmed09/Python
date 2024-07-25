# Python Constructor:
# A constructor is a special type of method (function) which is used to initialize the instance members of the class.
# Constructors can be of two types.
# Parameterized Constructor, Non-parameterized Constructor.


# Creating the constructor in python:
# the method __init__ simulates the constructor of the class. This method is called when the class is instantiated.
class Employee:
    def __init__(self, name, id):
        self.id = id
        self.name = name

    def display(self):
        print("ID: %d \nName: %s" % (self.id, self.name))


emp1 = Employee("John", 101)
emp2 = Employee("David", 102)
emp1.display()  # accessing display() method to print employee 1 information
emp2.display()  # accessing display() method to print employee 2 information
print()


# Example: Counting the number of objects of a class
class Student:
    count = 0

    def __init__(self):
        Student.count = Student.count + 1


s1 = Student()
s2 = Student()
s3 = Student()
print("The number of students:", Student.count)
print()


# Python Non-Parameterized Constructor Example
class Student:
    # Constructor - non parameterized
    def __init__(self):
        print("This is non parametrized constructor")

    def show(self, name):
        print("Hello", name)


student = Student()
student.show("John")
print()


# Python Parameterized Constructor Example
class Student:
    # Constructor - parameterized
    def __init__(self, name):
        print("This is parametrized constructor")
        self.name = name

    def show(self):
        print("Hello",self.name)


student = Student("John")
student.show()
print()


# Python In-built class functions:
class Student:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age


s = Student("John", 101, 22)  # creates the object of the class Student

print(getattr(s, 'name'))  # prints the attribute name of the object s

setattr(s, "age", 23)  # reset the value of attribute age to 23

print(getattr(s, 'age'))  # prints the modified value of age

print(hasattr(s, 'id'))  # prints true if the student contains the attribute with name id

delattr(s, 'age')  # deletes the attribute age

# print(s.age)  # this will give an error since the attribute age has been deleted
print()


# Built-in class attributes:
class Student:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age

    def display_details(self):
        print("Name:%s, ID:%d, age:%d" % (self.name, self.id))


s = Student("John", 101, 22)
print(s.__doc__)
print(s.__dict__)
print(s.__module__)
