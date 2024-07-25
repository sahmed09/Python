from functools import reduce
# The map() function executes a specified function for each item in a iterable.
# The item is sent to the function as a parameter.
print("map function: ")


def myfunc(n):
    return len(n)


x = map(myfunc, ('apple', 'banana', 'cherry'))
print(x)
print(list(x))  # convert the map into a list, for readability


def myfunc(a, b):
  return a + b


x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

print(x)
print(list(x))  # convert the map into a list, for readability
print()

numbers = ['34', '3', '65']
numbers = list(map(int, numbers))
print(numbers[2] + 5)


def sq(a):
    return a*a


num = [2, 3, 5, 9, 23, 6, 3, 2]
square = list(map(sq, num))
print(square)

num = [2, 3, 5, 9, 23, 6, 3, 2]
square = list(map(lambda x: x*x, num))
print(square)
print()


def squ(a):
    return a*a


def cube(a):
    return a*a*a


func = [squ, cube]
for i in range(5):
    val = list(map(lambda x: x(i), func))
    print(val)
print()


# The filter() function returns an iterator were the items are filtered through a function to test
# if the item is accepted or not.
print("filter function:")
ages = [5, 12, 17, 18, 24, 32]


def myFunc(x):
    if x < 18:
        return False
    else:
        return True


adults = filter(myFunc, ages)

for x in adults:
    print(x, end=" ")
print("\n")

# It is normally used with Lambda functions to separate list, tuple, or sets.
# a list contains both even and odd numbers.
seq = [0, 1, 2, 3, 5, 8, 13]

# result contains odd numbers of the list
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))
# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))
print()


# function that filters vowels
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if variable in letters:
        return True
    else:
        return False


# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

# using filter function
filtered = filter(fun, sequence)

print('The filtered letters are:')
for s in filtered:
    print(s, end=" ")
print("\n")


# The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the
# list elements mentioned in the sequence passed along.This function is defined in “functools” module.
print("reduce function:")
# from functools import reduce
ll = [1, 2, 3, 4, 7]
num = reduce(lambda x, y: x+y, ll)  # using reduce to compute sum of list
print(num)

maximum = reduce(lambda a, b: a if a > b else b, ll)  # using reduce to compute maximum element from list
print(maximum)
