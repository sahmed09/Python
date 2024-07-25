import copy

"""="""
print("=")
lst1 = [1, 2, 3, 4]
lst2 = lst1
print(lst1, lst2)

lst2[1] = 50
print(lst1, lst2)
print()

"""copy() --> Shallow Copy"""
print("Shallow copy")
lst1 = [1, 2, 3, 4]
lst2 = lst1.copy()
print(lst1, lst2)

lst2[1] = 50
print(lst1, lst2)
print()

"""Shallow Copy nested list
In nested list, while using .copy() if we use append() operation in any list, the same thing will not happen to other 
list. But if we alter any value of a list, the same value will be altered in the other list."""
print("Shallow Copy nested list")
lst1 = [[1, 2, 3, 4], [5, 6, 7, 8]]
lst2 = lst1.copy()
print(lst1, lst2)

lst2[1][0] = 50
print(lst1, lst2)

lst1.append([9, 10, 11, 12])
print(lst1, lst2)

lst2.append([21, 22])
print(lst1, lst2)
print()

"""Deep copy -> using import copy
In a normal list, shallow copy == deep copy"""
print("Deep copy")
lst1 = [1, 2, 3, 4]
lst2 = copy.deepcopy(lst1)
print(lst1, lst2)

lst2[1] = 100
print(lst1, lst2)
print()

"""Deep Copy nested list"""
print("Deep Copy nested list")
lst1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lst2 = copy.deepcopy(lst1)
print(lst1, lst2)

lst2[1][0] = 100
print(lst1, lst2)

lst1.append([10, 11, 12])
print(lst1, lst2)

lst2.append([4, 5])
print(lst1, lst2)
