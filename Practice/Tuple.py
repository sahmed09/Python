# A tuple is a collection which is ordered and unchangeable. Allows duplicate members
thistuple = ("apple", "banana", "cherry")
print(thistuple)

print(len(thistuple))  # Tuple Length

# Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
print(thistuple[-1])  # Negative Indexing
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])  # Range of Indexes
print(thistuple[-4:-1])  # Range of Negative Indexes. index -4 (included) to index -1 (excluded)

# Change Tuple Values
# Tuples are unchangeable, or immutable.
# You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)  # converting tuple to list
y[1] = "kiwi"  # changing list value
x = tuple(y)  # # converting list to tuple
print(x)

# Loop Through a Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

# Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

x = "kiwi" in thistuple
print(x)

# Add Items
# Once a tuple is created, you cannot add items to it. Tuples are unchangeable.

# Create Tuple With One Item
# To write a tuple containing a single value, have to include a comma, even though there is only one value
thistuple = ("apple",)  # tuple
print(type(thistuple))

thistuple = ("apple")  # not a tuple
print(type(thistuple))

# Remove Items
# Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely
thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple)  # #this will raise an error because the tuple no longer exists

# Join Two Tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "banana", "apple")
print(thistuple.count("apple"))  # Returns the number of times a specified value occurs in a tuple

print(thistuple.index("apple"))  # Searches the tuple for a specified value and returns the position where it was found
print("Index of apple from the beginning =", thistuple.index("apple"))
print("Index of apple within a range =", thistuple.index("apple", 2, 4))
print("Index of apple from from 4 =", thistuple.index("apple", 4))
print()

# Nesting List and tuple:
Employees = [(101, "Ayush", 22), (102, "john", 29), (103, "james", 45), (104, "Ben", 34)]
print("----Printing list----")
for i in Employees:
    print(i)
Employees[0] = (110, "David",22)
print()
print("----Printing list after modification----")
for i in Employees:
    print(i)
print()

(x, y) = (22, 33)
print(x)
print(y)

# Comparing tuples:
# Python starts by comparing the first element from each sequence. If they are equal, it goes on to the next element,
# and so on, until it finds elements that differ.
print((2, 3, 5) < (5, 6, 5))
print(('Jones', 'Sally') < ('Jones', 'Sam'))

# Sorting Tuple:
d = {'a': 10, 'b': 1, 'c': 22}
print(d.items())
print(sorted(d.items()))  # Using sorted()
for k, v in sorted(d.items()):  # Using sorted()
    print(k, v)

# Sort by values instead of keys:
d = {'a': 10, 'b': 1, 'c': 22}
tmp = list()
for k, v in d.items():
    tmp.append((v, k))
print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)
