# An iterator is an object that contains a countable number of values.
# in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
# Lists, tuples, dictionaries, and sets are all iterable objects.
# All these objects have a iter() method which is used to get an iterator
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)  # Return an iterator from a tuple, and print each value:
print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"  # Strings are also iterable objects, containing a sequence of characters
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Looping Through an Iterator
mytuple = ("apple", "banana", "cherry")  # Iterate the values of a tuple
for x in mytuple:
    print(x)

mystr = "banana"  # Iterate the characters of a string
for x in mystr:
    print(x)

# Create an Iterator
# To create an object/class as an iterator, implement the methods __iter__() and __next__() to your object.
# The __iter__() method allows to do operations (initializing etc.), but must always return the iterator object itself.
# The __next__() method also allows to do operations, and must return the next item in the sequence.
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


# StopIteration
# To prevent the iteration to go on forever, we can use the StopIteration statement.
# In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
