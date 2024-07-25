"""A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements. Each element
or value that is inside of a list is called an item. Just as strings are defined as characters between quotes, lists
are defined by having values between square brackets [ ]. List allows duplicate members."""

lst = list()
print(type(lst))
print(dir(lst))

lst = ['mathematics', 'physics', 100, 200, 10.5, 20.5]
print(lst)
print(len(lst))

# append is used to add elements in the list
lst.append('Shihab')
print(lst)

lst.append(['X', 'Y'])
print(lst)

# Indexing in List
print(lst[7])
print(lst[2:4])

# insert in a specific order
lst.insert(2, 'chemistry')
print(lst)

# Extend method
lst.extend([8, 9])
print(lst)

# Various Operations that we can perform in List
lst = [8, 9, 6, 10, 11, 4]
print(lst)
print(sum(lst))

lst = [1, 2, 3]
print(lst * 3)

# Pop() Method
print(lst.pop())
print(lst)
print(lst.pop(0))
print(lst)

# count():Calculates total occurrence of given element of List
lst = [1, 1, 2, 3, 4, 5]
print(lst.count(1))

# length:Calculates total length of List
print(len(lst))

# index(): Returns the index of first occurrence. Start and End index are not necessary parameters
print(lst.index(1, 1, 4))  # (value, start, end)  -> start and end are not necessary

# Min and Max
print(min(lst))
print(max(lst))
