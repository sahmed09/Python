# if
print("if")
a = 33
b = 200
if b > a:
    print("b is greater than a")

# elif
print("\nelif")
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# else
print("\nelse")
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Short Hand If
print("\nShort Hand If")
a = 200
b = 33
if a > b: print("a is greater than b")

# Short Hand If ... Else
print("\nShort Hand If ... Else")
a = 2
b = 330
print("A") if a > b else print("B")  # This technique is known as Ternary Operators, or Conditional Expressions.

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# And
print("\nAnd")
a = 200
b = 33
c = 500
if a > b and c > b:
    print("Both conditions are true")

# Or
print("\nOr")
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")

# Nested If
print("\nNested If")
x = 40
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# The pass Statement
"""
if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
"""
print("\nThe pass Statement")
a = 33
b = 200
if b > a:
    pass
