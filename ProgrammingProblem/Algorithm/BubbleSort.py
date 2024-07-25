"""Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if
they are in wrong order."""


def bubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# Driver code to test above:
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")
print("\n")

# The above function always runs O(n^2) time even if the array is sorted.
# It can be optimized by stopping the algorithm if inner loop didn't cause any swap.


# Optimized Implementation:
def bubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # IF no two elements were swapped by inner loop, then break
        if not swapped:
            break


# Driver code to test above:
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")
print("\n")

"""
Worst and Average Case Time Complexity: O(n*n). Worst case occurs when array is reverse sorted.
Best Case Time Complexity: O(n). Best case occurs when array is already sorted.
Auxiliary Space: O(1)
Boundary Cases: Bubble sort takes minimum time (Order of n) when elements are already sorted."""


# Recursive Bubble Sort:
def bubbleSort(listt):
    for i, num in enumerate(listt):
        try:
            if listt[i+1] < num:
                listt[i] = listt[i+1]
                listt[i+1] = num
                bubbleSort(listt)
        except IndexError:
            pass
    return listt


listt = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(listt)

print("Sorted Array:")
for i in range(0, len(listt)):
    print(listt[i], end=" ")
print('\n')


def bubbleSort(arr, n):
    for i in range(1, n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    n = len(arr)

    print("Before Sorting: ")
    print(arr)

    bubbleSort(arr, n)

    print("After Sorting: ")
    print(arr)
