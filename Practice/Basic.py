import random
# Single line comment
"""
Multi line comment
"""
'''
Multi line Comment
'''
# camel case --> Used in other languages
ageOfHello = 2+2
print(ageOfHello, type(ageOfHello))

# snake case --> Used in Python
hello_world = 'And or now'  # string
print(hello_world, type(hello_world))

hel = " or then"
print(hello_world + hel)  # string join
a = True
print(a, type(a))

print(11/2)
print(int(11/2))  # type casting
print(11 % 2)
print(11.5 % 3)

x = 10
x = -x
print(x)
print(abs(x))

# Standard data types:
# Numbers, String, List, Tuple, Dictionary

# Python Literals:
# Literals can be defined as a data that is given in a variable or constant.
# I. String literals: text1='hello'
# II.Numeric literals:
# III. Boolean literals:
# IV. Special literals: Python contains one special literal i.e., None.
# V.Literal Collections: Collections such as tuples, lists and Dictionary are used in Python.

# divmod operator
x = 10
y = 3
result = divmod(x, y)  # divmod used when both quotient and remainder are needed
print(result)  # (3,1) 3 is quotient and 1 is remainder

# exponential operator
x = 2
result = x ** 4
print(result)
y = 2
result = pow(y, 4)
print(result)

# static type language --> java,c,c++ coz variable type should be declared
# duck type --> python, variable type declaration not necessary

t, y, u = 10, 15, 20
print(t, u, y)

f = 3j
print(f, type(f))

print(random.randrange(1, 10))

# taking input
"""x = int(input("Enter a number : "))
print(x)
print(type(x))"""

print(bool("Hello"))
print(bool("True"))
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


class MyClass:

    def __len__(self):
        return 0


myObj = MyClass()
print(bool(myObj))


def myfunction():
    return True


print(myfunction())


def myFunction() :
    return True


if myFunction():
    print("YES!")
else:
    print("NO!")


# isinstance() function is a built-in functions that returns a boolean value
# which can be used to determine if an object is of a certain data type
x = 200
print(isinstance(x, int))

# Python Membership Operators:
print("Python Membership Operators : ")
a = 10
b = 20
ll = [1, 2, 3, 4, 5]

if a in ll:
    print("Line 1 - a is available in the given list")
else:
    print("Line 1 - a is not available in the given list")

if b not in ll:
    print("Line 2 - b is not available in the given list")
else:
    print("Line 2 - b is available in the given list")

# Python Identity Operators:
print("Python Identity Operators : ")
a = 20
b = 20

if a is b:
    print("Line 1 - a and b have same identity")
else:
    print("Line 1 - a and b do not have same identity")

if id(a) == id(b):
    print("Line 2 - a and b have same identity")
else:
    print("Line 2 - a and b do not have same identity")

b = 30
if a is b:
    print("Line 3 - a and b have same identity")
else:
    print("Line 3 - a and b do not have same identity")

a = 2
b = 8
print(a, b)
a, b = b, a
print(a, b)
"""
temp = a
a = b
b = temp
"""

"""0=00, 1=01, 2=10, 3=11"""
print(0 & 1)
print(2 & 3)
print(0 | 1)
print(2 | 3)
print()

# 'is' vs '==':
# is - reference equality - two references refer to the same object.
# == - value equality - two objects have the same value.
a = [6, 9, 3, 2]
b = a
print("b == a :", b == a)
print("b is a :", b is a)
print("a is b :", a is b)
print(id(a), id(b))
b[0] = 0
print("a: ", a)
print(id(a), id(b))
c = a[:]
print("c:", c)
print("c is a :", c is a)
print(id(a), id(c))

a = [3, 6, "36"]
b = [3, 6, "36"]
print(a is b, id(a), id(c))
print(b is a, id(a), id(c))
