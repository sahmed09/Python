"""Zip Functions:
1. Able to iterate through multiple iterables
2. It is and iterable. So we can use for loop, next() method to iterate elements
3. We can use it efficiently in data preprocessing, feature engineering as we can do parallel iteration through
multiple iterables."""

lst1 = ['Shihab', 'Ahmed', 'X']
lst2 = ['a', 'b', 'c']

result = zip(lst1, lst2)
print(result)

print(list(result))

# zip object is an iterator
# print(next(result))

result = zip(lst1, lst2)
for i, j in result:
    print(i, j)
print()

lst1 = ['Shihab', 'Ahmed', 'X']
lst2 = ['a', 'b', 'c']
lst3 = [1, 2, 3]
result = zip(lst1, lst2, lst3)
for i, j, k in result:
    print(i, j, k)
print()

lst1 = ['Shihab', 'Ahmed', 'X', 'Y', 'Z']
lst2 = ['a', 'b', 'c']
lst3 = [1, 2, 3]
result = zip(lst1, lst2, lst3)
for i, j, k in result:
    print(i, j, k)
print()

dict1 = {'name': 'Shihab', 'l_name': 'Ahmed', 'Age': 25}
dict2 = {'name': 'X', 'l_name': 'Y', 'Age': 20}
print(dict1.items())
dictionary = zip(dict1.items(), dict2.items())
print(dictionary)

for (i, j), (i2, j2) in dictionary:
    print(i, j)
    print(i2, j2)
