# Generator-Function :
# A generator-function is defined like a normal function, but whenever it needs to generate a value,
# it does so with the yield keyword rather than return.
# If the body of a def contains yield, the function automatically becomes a generator function.
print("Generator-Function:")


def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


for value in simpleGeneratorFun():
    print(value)
print()

# Generator-Object :
# Generator functions return a generator object. Generator objects are used either by calling the next method
# on the generator object or using the generator object in a “for in” loop.
print("Generator-Object :")


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
