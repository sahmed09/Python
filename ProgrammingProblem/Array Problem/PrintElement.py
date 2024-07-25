"""Python program to print the elements of an array"""

arr = [1, 2, 3, 4, 5]

# Loop through the array by incrementing the value of i
print("Elements of given array: ")
for i in range(0, len(arr)):
    print(arr[i], end=" ")

print("\n")


"""Python program to print the elements of an array in reverse order"""

arr = [1, 2, 3, 4, 5]

# Loop through the array by incrementing the value of i
print("Original array: ")
for i in range(0, len(arr)):
    print(arr[i], end=" ")

# Loop through the array in reverse order
print("\nArray in reverse order: ")
for i in range(len(arr)-1, -1, -1):
    print(arr[i], end=" ")
