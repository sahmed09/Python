# Calling a Function
def my_function():
    print("Hello from a function")


my_function()


# Types of arguments:
# 1.Required arguments, 2.Keyword arguments, 3.Default arguments, 4.Variable-length arguments

# 1.Required Arguments:
def my_function(fname):
    print(fname + " Rafsnes")


my_function("Shihab")
my_function("Tithi")


# Call by reference in Python:
# In python, all the functions are called by reference,
# all the changes made to the reference inside the function revert back to the original value referred by the reference.
# Passing Immutable Object(List)
def change_list(list1):  # defining the function
    list1.append(20)
    list1.append(30)
    print("list inside function = ", list1)


list1 = [10, 30, 40, 50]  # defining the list
change_list(list1)  # calling the function
print("list outside function = ", list1)


# Passing Mutable Object (String):
def change_string(stri):  # defining the function
    stri = stri + " Hows you"
    print("printing the string inside function :", stri)


string1 = "Hi I am there"
change_string(string1)  # calling the function
print("printing the string outside function :", string1)


# Number of Arguments
def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Emil", "Refsnes")


# 4.Arbitrary Arguments, *args (Variable-length arguments)
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly
def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


def my_function(*kids):
    print(type(kids))
    print("The youngest child is " + kids[0])
    for item in kids:
        print(item, end=" ")
    print()


har = ["Emil", "Tobias", "Linus"]
my_function(*har)


# 2.Keyword Arguments : send arguments with the key = value syntax
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")


# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly
def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")


def my_function(**kids):
    print(type(kids))
    for key, value in kids.items():
        print(key, value)
    print()


har = {"name": "Emil", "age": 25}
my_function(**har)


# 3.Default Parameter Value
# If we call the function without argument, it uses the default value
def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function()  # it will use the default value


# Passing a List as an Argument
# if you send a List as an argument, it will still be a List when it reaches the function
def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)


# Return Values
def my_function(x):
    return x * 5


print(my_function(5))
print(my_function(4))


# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error
def my_function():
    pass


# Recursion
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0

    return result


print("\n\nRecursion Example Results")
tri_recursion(6)


def fnc():
    """Docstring: First line string written inside a function"""
    pass


print(fnc.__doc__)
print()


# order to pass normal arguments, args, kwargs:
def master(normal, *args, **kwargs):
    print(normal)
    for i in args:
        print(i, end=" ")
    print()
    for key, value in kwargs.items():
        print(key, value)


lis = ["Shihab", 22, 263986]
marklist = {"Shihab": 99, "Ahmed": 98, "Apu": 97, "SA": 96}
# print(master("normal arge", *lis, **marklist))
master("normal arge", *lis, **marklist)
