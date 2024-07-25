"""Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself for the two
halves and then merges the two sorted halves. """


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        # mid = l + (r-1)/2
        L = arr[:mid]  # Dividing the array elements into 2 halves
        R = arr[mid:]

        mergeSort(L)  # Sorting the first half... Recursion calls till left<right
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# driver code to test the above code
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7, 1]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
    print()


# Alternative Method:
def merge_sort(values):

    if len(values) > 1:
        m = len(values) // 2
        # mid = l + (r-1)/2
        left = values[:m]
        right = values[m:]
        left = merge_sort(left)
        right = merge_sort(right)

        values = []

        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                values.append(left[0])
                left.pop(0)
            else:
                values.append(right[0])
                right.pop(0)

        for i in left:
            values.append(i)
        for i in right:
            values.append(i)

    return values


# Input list
a = [12, 11, 13, 5, 6, 7, 1]
print("Given array is")
print(*a)

a = merge_sort(a)

# Print output
print("Sorted array is : ")
print(*a)

"""
Time Complexity: Merge Sort is a recursive algorithm and time complexity can be expressed as following recurrence 
relation: T(n) = 2T(n/2) + Theta(n)
The above recurrence can be solved either using Recurrence Tree method or Master method. It falls in case II of 
Master Method and solution of the recurrence is Theta(nLogn).
Time complexity of Merge Sort is Theta(nLogn) in all 3 cases (worst, average and best) as merge sort always 
divides the array into two halves and take linear time to merge two halves.
Auxiliary Space: O(n)
Algorithmic Paradigm: Divide and Conquer
Sorting In Place: No in a typical implementation
Stable: Yes
"""
