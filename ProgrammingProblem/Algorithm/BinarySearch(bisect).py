from bisect import bisect_left  # Returns leftmost insertion point of x in a sorted list.
from bisect import bisect_right  # Returns rightmost insertion point of x in a sorted list a.


# Finding first occurrence of an element:
def binary_search(arr, x):
    i = bisect_left(arr, x)

    if i != len(arr) and arr[i] == x:
        return i
    else:
        return -1


arr = [1, 2, 4, 4, 8]
x = 4
res = binary_search(arr, x)
if res == -1:
    print(x, "is absent")
else:
    print("First occurrence of", x, "is present at", res)
print()


# Finding greatest value smaller than x:
def binary_search(arr, x):
    i = bisect_left(arr, x)

    if i:
        return i - 1
    else:
        return -1


arr = [1, 2, 4, 4, 8]
x = 7
res = binary_search(arr, x)
if res == -1:
    print("No value smaller than ", x)
else:
    print("Largest value smaller than ", x, " is at index ", res)
print()


# Finding rightmost occurrence:
def binary_search(arr, x):
    i = bisect_right(arr, x)

    if i != len(arr)+1 and arr[i-1] == x:
        return i-1
    else:
        return -1


arr = [1, 2, 4, 4, 8]
x = 4
res = binary_search(arr, x)
if res == -1:
    print(x, "is absent")
else:
    print("Last  occurrence of", x, "is present at", res)
