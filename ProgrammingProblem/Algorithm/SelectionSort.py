"""The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order)
from unsorted part and putting it at the beginning."""


def selection_sort(arr):
    for i in range(len(arr)):
        # Find the minimum element in remaining unsorted array
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


A = [64, 25, 12, 22, 11]

result = selection_sort(A)
# print(result)

print("Sorted array:")
for i in result:
    print(i, end=" ")

# Time Complexity: O(n^2) as there are two nested loops.
# Auxiliary Space: O(1)
