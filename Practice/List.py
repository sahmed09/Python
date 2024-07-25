# List is a collection which is ordered and changeable. Allows duplicate members
thislist = ["apple", "banana", "cherry"]
print(thislist)

# Access items
print(thislist[1])
print(thislist[-1])  # Negative Indexing
print()

# Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])  # Range of Negative Indexes. index -4 (included) to index -1 (excluded)
print(thislist[::2])
print()

# Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

x = "banana" in thislist
print(x)

# List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# Add Items
newlist = ["apple", "banana", "cherry"]
newlist.append("orange")  # To add an item to the end of the list, use the append() method
print(newlist)

newlist.insert(1, "watermelon")  # To add an item at the specified index, use the insert() method
print(newlist)

# Remove Item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")  # The remove() method removes the specified item
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()  # The pop() method removes the specified index, (or the last item if index is not specified)
print(thislist)

thislist.pop(0)
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[1]  # The del keyword removes the specified index
print(thislist)

del thislist  # The del keyword can also delete the list completely

thislist = ["apple", "banana", "cherry"]
thislist.clear()  # The clear() method empties the list
print(thislist)

# Copy a List
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()  # Make a copy of a list with the copy() method
print(mylist)

ll = ["apple", "banana", "cherry"]
nl = list(ll)  # Make a copy of a list with the built-in method list()
print(nl)

# Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2  # using the + operator
print(list3)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)  # appending all the items from list2 into list1, one by one
print(list1)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)  # extend() method to add list2 at the end of list1
print(list1)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list2.extend(list1)  # Add the elements of a list (or any iterable), to the end of the current list
print(list2)

# The list() Constructor
# It is also possible to use the list() constructor to make a new list
thislist = list((1, 2, 3))
print(thislist)

llist = [1, 2, 3, 4, 5, 1, 2, 1]
print(llist.count(1))  # Returns the number of elements with the specified value
print("Index of 1 from the beginning is ", llist.index(1))
print("Index of 1 from 6 is ", llist.index(1, 6))  # Returns the index of the first element with the specified value
print("Index of 1 within a range is ", llist.index(1, 3, 6))

llist.reverse()  # Reverses the order of the list
print(llist)

# Sort the list
nl = [1, 2, 3, 4, 5, 1, 2, 1]
nl.sort()  # Sorts the list
print(nl)

nl = ["adsd", "asaf", "eref", "dafw"]
print(range(len(nl)))
print(dir(nl))

nl = [1, 2, 3, 4, 5, 1, 2, 1]
print("max:", max(nl))
print("min:", min(nl))
print("sum:", sum(nl))
print("avg:", sum(nl)/len(nl))
print(any(nl))

abc = "With three words"
print(abc.split())
print(any(abc))

# List Methods
"""
.append(obj)
.count(obj)
.extend(seq)
.index(obj)
.reverse()
.remove(obj)
.pop(obj=list[-1])
.insert(index, obj)
.sort([func])
"""

lis = list(map(str, input("Enter ").split()))
print(lis[0])
print(lis[1])
print(lis[2])
