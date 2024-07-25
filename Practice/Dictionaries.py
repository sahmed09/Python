# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members
# In Python dictionaries are written with curly brackets, and they have keys and values
from collections import OrderedDict

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

print(len(thisdict))  # Dictionary Length

# Accessing Items
# We can access the items of a dictionary by referring to its key name, inside square brackets
x = thisdict["year"]  # Get the value of the "year" key
print(x)

x = thisdict.get("model")  # using get() method
print(x)

# If key doesn't exist, it will raise error. Here 0  is the default value and using this we can handle the error
# and if the key doesnt exist, it will return default value. In this case it's 0
x = thisdict.get("parts", 0)
print(x)

# Change Values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 1983
print(thisdict)

# Loop Through a Dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict:
    print(x)  # Print all key names in the dictionary, one by one

for x in thisdict:
    print(thisdict[x])  # Print all values in the dictionary, one by one

for x in thisdict.values():
    print(x)  # also use the values() method to return values of a dictionary

for x, y in thisdict.items():
    print(x, y)  # Loop through both keys and values, by using the items() method

# Check if Key Exists
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
x = "age" in thisdict
print(x)

# Adding Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
thisdict.update({"wheel": 6})
print(thisdict)

# Removing Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")  # The pop() method removes the item with the specified key name
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead)
thisdict.popitem()
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]  # The del keyword removes the item with the specified key name
print(thisdict)

del thisdict  # The del keyword can also delete the dictionary completely
# print(thisdict)  # this will cause an error because "thisdict" no longer exists.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()  # The clear() method empties the dictionary
print(thisdict)

# Copy a Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()  # Make a copy of a dictionary with the copy() method
print(mydict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)  # Make a copy of a dictionary with the dict() function
print(mydict)

# Nested Dictionaries
# A dictionary can also contain many dictionaries, this is called nested dictionaries
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
print(myfamily)

# if you want to nest three dictionaries that already exists as dictionaries
# Create three dictionaries, then create one dictionary that will contain the other three dictionaries
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
  "name": "Tobias",
  "year": 2007
}
child3 = {
  "name": "Linus",
  "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myfamily)

# The dict() Constructor
# It is also possible to use the dict() constructor to make a new dictionary
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict.keys())
print(thisdict.values())

b = [True, False, int, float, "apple", "banana", "cherry", 6, 22, 68, 90, 25]
for item in b:
    if str(item).isnumeric() and item > 6:
        print(item, end=" ")
print()

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqain', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqain', 'cwen']
for name in names:
    counts[name] = counts.get(name, 3) + 1
print(counts)

child = {"name": "Emil", "year": 2004}
print(list(child))
print(child.keys())
print(child.values())
print(child.items())
