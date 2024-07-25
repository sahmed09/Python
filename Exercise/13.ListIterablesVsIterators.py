# Iterables. List is iterable.
lst = [1, 2, 3, 4, 5]
for i in lst:
    print(i)

# Iterator: iter() converts a list into an iterator
# An iterator is an object that contains a countable number of values.
# In Python, an iterator is an object which implements the iterator protocol, which consist of the
# methods __iter__() and __next__().
# Lists, tuples, dictionaries, and sets are all iterable objects.
# All these objects have a iter() method which is used to get an iterator.
res = iter(lst)
print(res)

lst = [1, 2, 3, 4, 5]
myit = iter(lst)
print(myit)
for i in myit:
    print(i)

mystr = "goal"  # Strings are also iterable objects, containing a sequence of characters
myit = iter(mystr)
print(myit)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)
print(myit)
for _ in range(len(mystr)):
    print(next(myit))
