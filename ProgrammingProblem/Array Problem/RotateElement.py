"""Python program to left rotate the elements of an array"""
# In the left rotation, each element of the array will be shifted to its left by one position
# and the first element of the array will be added to end of the list.

arr = [1, 2, 3, 4, 5]

# n determine the number of times an array should be rotated
n = 3

# Displays original array
print("Original array: ")
for i in range(0, len(arr)):
    print(arr[i], end=" ")

# Rotate the given array by n times toward left
for i in range(0, n):
    # Stores the first element of the array
    first = arr[0]

    for j in range(0, len(arr)-1):
        # Shift element of array by one
        arr[j] = arr[j+1]

    # First element of array will be added to the end
    arr[len(arr)-1] = first

print()

# Displays resulting array after rotation
print("Array after left rotation: ")
for i in range(0, len(arr)):
    print(arr[i], end=" ")
print("\n")
# 2 3 4 5 1 -> 3 4 5 1 2 -> 4 5 1 2 3


"""Python program to right rotate the elements of an array"""
# An array is said to be right rotated if all elements of the array are moved to its right by one position.
# The last element of the array will become the first element of the rotated array.

arr = [1, 2, 3, 4, 5]

# n determine the number of times an array should be rotated
n = 3

# Displays original array
print("Original array: ")
for i in range(0, len(arr)):
    print(arr[i], end=" ")

# Rotate the given array by n times toward right
for i in range(0, n):
    # Stores the last element of the array
    last = arr[len(arr)-1]

    for j in range(len(arr)-1, -1, -1):
        # Shift element of array by one
        arr[j] = arr[j-1]

    # Last element of the array will be added to the start of the array.
    arr[0] = last

print()

# Displays resulting array after rotation
print("Array after right rotation: ")
for i in range(0, len(arr)):
    print(arr[i], end=" ")
# 5 1 2 3 4 -> 4 5 1 2 3 -> 3 4 5 1 2
