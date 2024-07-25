"""Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the
given array around the picked pivot."""

# This function takes last element as pivot, places the pivot element at its correct position in sorted array,
# and places all smaller (smaller than pivot) to left of pivot and all greater elements to right of pivot


def partition(arr, low, high):
    i = low - 1  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than the pivot
        if arr[j] < pivot:

            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:

        # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr, low, high)

        # Separately sort elements before partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


# Driver code to test above
if __name__ == '__main__':
    arr = [10, 7, 8, 9, 1, 5, 4]
    n = len(arr)
    quickSort(arr, 0, n-1)  # Calling quickSort function
    print("Sorted array is:")
    for i in range(n):
        print(arr[i], end=" ")
    print("\n")


# iterative implementation:
def partition(arr, low, high):
    i = low - 1  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than the pivot
        if arr[j] <= pivot:

            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


# Function to do Quick sort
# arr[] --> Array to be sorted,
# l  --> Starting index,
# h  --> Ending index

def quickSortIterative(arr, low, high):

    # Create an auxiliary stack
    size = high - low + 1
    stack = [0] * size

    # initialize top of stack
    top = -1

    # push initial values of l and h to stack
    top = top+1
    stack[top] = low
    top = top+1
    stack[top] = high

    # Keep popping from stack while is not empty
    while top >= 0:

        # Pop high and low
        high = stack[top]
        top = top-1
        low = stack[top]
        top = top-1

        # Set pivot element at its correct position in sorted array
        p = partition(arr, low, high)

        # If there are elements on left side of pivot, then push left side to stack
        if p-1 > low:
            top = top+1
            stack[top] = low
            top = top+1
            stack[top] = p-1

        # If there are elements on right side of pivot, then push right side to stack
        if p+1 < high:
            top = top + 1
            stack[top] = p+1
            top = top + 1
            stack[top] = high


# Driver code to test above
arr = [4, 3, 5, 2, 1, 3, 2, 3, 10]
n = len(arr)
quickSortIterative(arr, 0, n-1)  # Calling quickSort function
print("Sorted array is:")
for i in range(n):
    print(arr[i], end=" ")
print()


"""Time taken by QuickSort in general can be written as following: T(n) = T(k) + T(n-k-1) + theta(n)
The first two terms are for two recursive calls, the last term is for the partition process. 
k is the number of elements which are smaller than pivot.
Worst Case: The worst case occurs when the partition process always picks greatest or smallest element as pivot.
    Following is recurrence for worst case. T(n) = T(0) + T(n-1) + theta(n)
    The solution of above recurrence is theta(n^2).
Best Case: The best case occurs when the partition process always picks the middle element as pivot.
    Following is recurrence for best case T(n) = 2T(n/2) + theta(n)
    The solution of above recurrence is theta(nLogn)
Average Case: To do average case analysis, we need to consider all possible permutation of array and calculate time 
    taken by every permutation which doesn’t look easy.
     Following is recurrence for this case. T(n) = T(n/9) + T(9n/10) + theta(n)
     Solution of above recurrence is also O(nLogn)"""
