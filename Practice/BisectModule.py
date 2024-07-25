import bisect  # list must be sorted to use bisect module

a = [1, 2, 4, 6, 7, 8, 9, 34]
print(a)
number = 5
print(bisect.bisect(a, number))  # returns the position where to insert the number

bisect.insort(a, number)  # insert the number in the specified position
print(a)
