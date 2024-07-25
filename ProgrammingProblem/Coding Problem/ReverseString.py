txt = "Hello World"[::-1]  # Create a slice that starts at the end of the string, and moves backwards.
# the slice statement [::-1] means start at the end of the string and end at position 0,
# move with the step -1, negative one, which means one step backwards.
print(txt)


# Using Function:
def my_function(x):
    return x[::-1]


txt = my_function("Hello World")
print(txt)
