import inspect


# Object Introspection:
# Know about a object, from which class it comes, type of the object, how it stored.
# The inspect module provides several useful functions to help get information about live objects such as
# modules, classes, methods, functions, tracebacks, frame objects, and code objects.
# Four main kinds of services provided by this module: type checking, getting source code,
# inspecting classes and functions, and examining the interpreter stack
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

print(type(karan))
print(id(karan))
print(dir(karan))
print()

print(inspect.getmembers(karan))
