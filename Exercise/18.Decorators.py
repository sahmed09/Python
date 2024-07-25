"""Function copy"""


def welcome():
    return "Welcome"


wel = welcome()
del welcome
print("Function copy:")
print(wel)
# welcome()
print()

"""Closures
Python closure is a nested function that allows us to access variables of the outer function even after the outer 
function is closed. As Python closures are used as callback functions, they provide some sort of data hiding. 
This helps us to reduce the use of global variables."""


def main_welcome(msg):
    def sub_welcome():
        print('Sub Welcome Starts')
        print(msg)
        print('Sub Welcome Ends')
    return sub_welcome()


print("Closures:")
main_welcome('Shihab')
print()

"""Closures & initial Decorators"""


def main_welcome(func):
    def sub_welcome():
        print('Sub Welcome Starts')
        # func()
        print(func([1, 2, 7, 4, 5, 3]))
        print('Sub Welcome Ends')
    return sub_welcome()


print("Closures & initial Decorators:")
# main_welcome(print)
main_welcome(len)
main_welcome(sum)
main_welcome(sorted)
print()

"""Decorators
Decorators are Python functions that allow us to wrap another function as an input and modify its behavior without 
altering (permanently modifying) the wrapped function's code. They are used to extend the behavior of a particular 
object, such as a class, method, or function.
By definition, a decorator is a function that takes another function and extends the behavior of the latter function 
without explicitly modifying it."""
print("Decorators:")


def main_welcome(func):
    def sub_welcome():
        print('Sub Welcome Starts')
        func()
        print('Sub Welcome Ends')
    return sub_welcome()


def sub_func():
    print("Sub Function as decorators")


main_welcome(sub_func)
print()


def main_welcome(func):
    def sub_welcome():
        print('Sub Welcome Starts')
        func()
        print('Sub Welcome Ends')
    return sub_welcome()


@main_welcome
def sub_func():
    print("Sub Function as Decorator!!!!")
