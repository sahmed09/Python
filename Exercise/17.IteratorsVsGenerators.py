import types
from collections.abc import Iterator

"""Difference between iterator and generator
1. To create iterator, we use iter() keyword and to create generator, we use function along with yield keyword.
2. Generator uses the yield keyword. It saves the local variable.
3. Generator in python helps us to write fast and compact code.
4. Python iterator is much more memory efficient."""

# List is iterable
lst = [1, 2, 3, 4]
iterable = iter(lst)  # iterator
print(iterable)
print(type(iterable))
for i in iterable:
    print(i)


# Generator
# Generator-Function:
# A generator-function is defined like a normal function, but whenever it needs to generate a value,
# it does so with the yield keyword rather than return.
# If the body of a def contains yield, the function automatically becomes a generator function.
def square(n):
    for i in range(n):
        yield i ** 2


print(square(3))
for i in square(3):
    print(i)

print(issubclass(types.GeneratorType, Iterator))  # Generator is also an Iterator
print()


def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


for value in simpleGeneratorFun():
    print(value)
print()


# Generator-Object:
# Generator functions return a generator object. Generator objects are used either by calling the next method
# on the generator object or using the generator object in a “for in” loop.
def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


x = simpleGeneratorFun()
print(x)
print(x.__next__())
print(x.__next__())
print(x.__next__())
print()

# A simple generator for Fibonacci Numbers
print("generator for Fibonacci Numbers")


def fib(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1
    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a+b


# Create a generator object
x = fib(5)
# Iterating over the generator object using next
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())

# Iterating over the generator object using for in loop.
print("\nUsing for in loop")
for i in fib(5):
    print(i)

"""
Iterable - __iter()__ or __getItem()__
Iterator - __next()__
Iteration - 
"""
