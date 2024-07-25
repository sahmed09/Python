# Anonymous Function. A function with  no name.

def addition(a, b):
    return a + b


val = addition(2, 3)
print(val)


add = lambda a, b: a + b
print(add(5, 6))

number = lambda a: a % 2 == 0
print(number(9))

three_values = lambda x, y, z: x + y + z
print(three_values(10, 15, 20))
