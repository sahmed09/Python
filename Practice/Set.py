# Set is a collection which is unordered and unindexed. No duplicate members.
thisset = {"pine", "apple", "banana", "cherry"}
print(thisset)
print(type(thisset))

print(len(thisset))  # Get the Length of a Set

# Access Items
# You cannot access items in a set by referring to an index, since sets are unordered the items has no index
# But you can loop through the set items using a for loop
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

print("banana" in thisset)
x = "x" in thisset
print(x)

# Change Items
# Once a set is created, you cannot change its items, but you can add new items

# Add Items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")  # To add one item to a set use the add() method
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])  # To add more than one item to a set use the update() method
print(thisset)

# Remove Item
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")  # If the item to remove does not exist, remove() will raise an error.
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("apple")  # If the item to remove does not exist, discard() will NOT raise an error.
print(thisset)

# can also use the pop(), method to remove an item, but this method will remove the last item
# sets are unordered, so you will not know what item that gets removed
# The return value of the pop() method is the removed item
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()  # Remove the last item by using the pop() method
print(x)  # deleted value
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.clear()  # The clear() method empties the set
print(thisset)

thisset = {"apple", "banana", "cherry"}
del thisset  # The del keyword will delete the set completely
# print(thisset)

# Join Two Sets
# Both union() and update() will exclude any duplicate items
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)  # The union() method returns a new set with all items from both sets
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)  # The update() method inserts the items in set2 into set1
print(set1)

# The set() Constructor
thisset = set(("apple", "banana", "cherry"))  # Using the set() constructor to make a set
print(thisset)

# Union of two Sets:
Days1 = {"Monday", "Tuesday", "Wednesday", "Thursday"}
Days2 = {"Friday", "Saturday", "Sunday"}
print(Days1 | Days2)  # printing the union of the sets using union | operator
print(Days1.union(Days2))  # printing the union of the sets using union() method

# Intersection of two sets:
set1 = {"Ayush", "John", "David", "Martin"}
set2 = {"Steve", "Milan", "David", "Martin"}
print(set1 & set2)  # prints the intersection of the two sets using & operator
print(set1.intersection(set2))  # prints the intersection of the two sets using intersection() method

# The intersection_update() method:
# The intersection_update() method removes the items from the original set that are not present in both the sets.
# it modifies the original set by removing the unwanted items, intersection() method returns a new set.
a = {"ayush", "bob", "castle"}
b = {"castle", "dude", "emyway"}
c = {"fuson", "gaurav", "castle"}
a.intersection_update(b, c)
print(a)

# Difference of two sets:
Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}
Days2 = {"Monday", "Tuesday", "Sunday"}
print(Days1 - Days2)  # {"Wednesday", "Thursday" will be printed} using subtraction ( - ) operator
print(Days1.difference(Days2))  # prints the difference of the two sets Days1 and Days2 using difference() method

# Set comparisons:
Days1 = {"Monday", "Tuesday", "Wednesday", "Thursday"}
Days2 = {"Monday", "Tuesday"}
Days3 = {"Monday", "Tuesday", "Friday"}

print(Days1 > Days2)  # Days1 is the superset of Days2 hence it will print true.
print(Days1 < Days2)  # prints false since Days1 is not the subset of Days2
print(Days2 == Days3)  # prints false since Days2 and Days3 are not equivalent
print()

# FrozenSets:
# The frozen sets are the immutable form of the normal sets,
# i.e., the items of the frozen set can not be changed and therefore it can be used as a key in dictionary.
# The elements of the frozen set can not be changed after the creation.
# The frozenset() method is used to create the frozenset object.
# The iterable sequence is passed into this method which is converted into the frozen set as a return type of the method.
Frozenset = frozenset([1,2,3,4,5])
print(type(Frozenset))
print("printing the content of frozen set...")
for i in Frozenset:
    print(i)
# Frozenset.add(6)  # gives an error since we cannot change the content of Frozenset after creation
print()

# Frozenset for the dictionary:
Dictionary = {"Name": "John", "Country": "USA", "ID": 101}
print(type(Dictionary))
Frozenset = frozenset(Dictionary)  #F rozenset will contain the keys of the dictionary
print(type(Frozenset))
for i in Frozenset:
    print(i)
print()

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
print(set1.isdisjoint(set2))
print(set1.issubset(set2))
print(set1.issuperset(set2))
print()

set1 = {"a", "b", "c", 1, 2, 3}
set2 = {1, 2, 3}
print(set1.isdisjoint(set2))
print(set1.issubset(set2))
print(set1.issuperset(set2))
