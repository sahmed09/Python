"""A tuple is a collection which is ordered and unchangeable. Allows duplicate members"""

# create an empty Tuples
my_tuple = tuple()
print(my_tuple)

my_tuple = ()
print(type(my_tuple))

my_tuple = ("Shihab", "Ahmed", "John")
print(my_tuple)
print(my_tuple[0])

my_tuple = ('Hello', 'World')
print(type(my_tuple))
print(my_tuple)

# Inbuilt function
print(my_tuple.count('Hello'))
print(my_tuple.index('Hello'))
