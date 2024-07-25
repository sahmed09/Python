"""
Evaluate the given source in the context of globals and locals.
The source may be a string representing a Python expression or a code object as returned by compile().
The globals must be a dictionary and locals can be any mapping, defaulting to the current globals and locals.
If only globals is given, locals defaults to it.
eval() function evaluate python expression which are written as strings."""

"""How does Eval worK?
1. Parse Python expression
2. compile into a byte code
3. Evaluate the python expression
4. It will return the result"""

print(eval('5*5'))  # eval(expression)
print(eval('5*5+7/2'))
# print(eval(input('Enter the expression: ')))  # len([1, 2, 3, 4, 5, 6, 7, 8]), sum([1, 2, 3, 4, 5])


def square_num(n):
    return n ** 2


print(eval('square_num(10)'))

var = compile("5*5", "<string>", "eval")  # Step 1, and 2 done by compile() internally while using the eval()
print(var)
print(eval(var))
print()

# Globals -> eval(expression, {global})
print(eval('x + 50 + x ** 2', {'x': 10}))

x = 20
print(eval('x + 50 + x ** 2', {'x': x}))

x, y = 100, 150
print(eval('x + y + z', {'x': x, 'y': y, 'z': 200}))

print(eval('x > y'))
print()

# Locals -> -> eval(expression, {global}, {local})
print(eval('a + b + c', {}, {'a': 10, 'b': 20, 'c': 30}))
