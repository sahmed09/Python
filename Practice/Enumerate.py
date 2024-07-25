items = ["Apple", "Banana", "Mango", "Orange", "Guava"]

i = 1
for item in items:
    if i % 2 != 0:
        print(item)
    i += 1
print()

# USing enumerate()
# Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object.
# It gives both index and object.

# printing the tuples in object directly.
for item in enumerate(items):
    print(item)
print()

# changing index and printing separately
for count, item in enumerate(items, 200):
    print(count, item)
print()

for index, item in enumerate(items):
    if index % 2 == 0:
        print(item)
