"""Python program to print the elements of an array present on even position"""

arr = [1, 2, 3, 4, 5]

# Loop through the array by incrementing the value of i by 2
print("Elements of given array present on even position: ")

# Here, i will start from 1 as first even positioned element is present at position 1.
for i in range(1, len(arr), 2):
    print(arr[i], end=" ")

print("\n")


"""Python program to print the elements of an array present on odd position"""

arr = [1, 2, 3, 4, 5]

# Loop through the array by incrementing the value of i by 2
print("Elements of given array present on odd position: ")

# Here, i will start from 0 as first odd positioned element is present at position 0.
for i in range(0, len(arr), 2):
    print(arr[i], end=" ")

print("\n")


"""Python program to print the largest element in an array"""

arr = [25, 11, 7, 75, 56]
max = arr[0]

for i in range(1, len(arr)):
    if arr[i] > max:
        max = arr[i]

print("Largest element present in given array: ", max)
print()

largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar
    # print('Loop:', itervar, largest)
print('Largest:', largest)
print()


"""Python program to print the smallest element in an array"""

arr = [25, 11, 7, 75, 56]
min = arr[0]

for i in range(1, len(arr)):
    if arr[i] < min:
        min = arr[i]

print("Smallest element present in given array: ", min)
print()

smallest = None
print('Before:', smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    # print('Loop:', itervar, smallest)
print('Smallest:', smallest)
print()


"""Python program to print the number of elements present in an array"""

arr = [1, 2, 3, 4, 5, 4, 5]

# Number of elements present in an array can be found using len()
print("Number of elements present in given array: ", len(arr))

