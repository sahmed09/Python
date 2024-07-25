# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# lambda arguments : expression
x = lambda a: a + 10
print(x(5))

# Lambda functions can take any number of arguments
x = lambda a, b: a * b
print(x(10, 5))

x = lambda a, b, c: a + b + c
print(x(5, 10, 15))


# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number.
def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)  # function that always doubles the number you send in
print(mydoubler(11))


def myfunc(n):
    return lambda a: a * n


mytripler = myfunc(3)  # unction that always triples the number you send in
print(mytripler(11))


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

# Use lambda functions when an anonymous function is required for a short period of time.


def table(n):
    return lambda a: a * n  # a will contain the iteration variable i and a multiple of n is returned at each function call


n = 10
b = table(n)  # the entered number is passed into the function table. b will contain a lambda function which is called again and again with the iteration variable i
for i in range(1, 11):
    print(n, "X", i, "=", b(i))  # #the lambda function b is called with the iteration variable i,


def a_first(a):
    return a[1]


a = [[1, 14], [5, 6], [8, 23]]
a.sort(key=a_first)
print(a)

a = [[1, 14], [5, 6], [8, 23]]
a.sort(key=lambda x: x[1])
print(a)
