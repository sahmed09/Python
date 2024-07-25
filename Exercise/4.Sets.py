"""A Set is an unordered collection data type that is iterable, mutable, and has no duplicate elements. Python's set
class represents the mathematical notion of a set. This is based on a data structure known as a hash table"""

# Defining an empty set
set_var = set()
print(set_var)
print(type(set_var))

set_var = {1, 2, 3, 4, 3}
print(set_var)

set_var = {"Avengers", "IronMan", 'Hitman'}
print(set_var)
type(set_var)

# Inbuilt function in sets
set_var.add("Hulk")
print(set_var)

set1 = {"Avengers", "IronMan", 'Hitman'}
set2 = {"Avengers", "IronMan", 'Hitman', 'Hulk2'}

# Union
print("Union:", set2.union(set1))

# Intersection
print("Intersection:", set2.intersection(set1))

# Difference
print("Difference:", set2.difference(set1))

print(set2)

# Difference update
print("Difference Update:", set2.difference_update(set1))
print(set2)
