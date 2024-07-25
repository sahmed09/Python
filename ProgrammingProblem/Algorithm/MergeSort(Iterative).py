# Recursive Python Program for merge sort:
def merge(left, right):
    if not len(left) or not len(right):
        return left or right

    result = []
    i, j = 0, 0

    while len(result) < len(left) + len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break

    return result


def mergesort(list):
    if len(list) < 2:
        return list

    middle = len(list) // 2
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])

    return merge(left, right)


seq = [12, 11, 13, 5, 6, 7]
print("Given array is")
print(seq)
print("\nSorted array is")
print(mergesort(seq))
print()


# Iterative Merge Sort (Bottom Up):  -> Error on code
# Unlike Iterative QuickSort, the iterative MergeSort doesn’t require explicit auxiliary stack.
def mergeSort(a):

    current_size = 1

    # Outer loop for traversing Each sub array of current_size
    while current_size < len(a) - 1:

        left = 0

        # Inner loop for merge call in a sub array
        # Each complete Iteration sorts the iterating sub array
        while left < len(a) - 1:
            # mid index = left index of sub array + current sub array size - 1
            mid = min((left + current_size - 1), (len(a) - 1))

            # (False result,True result)[Condition] Can use current_size if 2 * current_size < len(a)-1 else len(a)-1
            right = ((2 * current_size + left - 1, len(a) - 1)[2 * current_size + left - 1 > len(a) - 1])

            # Merge call for each sub array
            merge(a, left, mid, right)
            left = left + current_size*2

            # Increasing sub array size by multiple of 2
            current_size = 2 * current_size


# Merge Function:
def merge(a, l, m, r):
    n1 = m-l+1
    n2 = r-m
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = a[l+i]
    for i in range(0, n2):
        R[i] = a[m+i+1]

    i, j, k = 0, 0, 1
    while i < n1 and j < n2:
        if L[i] > R[j]:
            a[k] = R[j]
            j += 1
        else:
            a[k] = L[i]
            i += 1
        k += 1

    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1


# Driver code
a = [12, 11, 13, 5, 6, 7]
print("Given array is ")
print(a)

mergeSort(a)

print("Sorted array is ")
print(a)

# Time complexity of above iterative function is same as recursive, i.e., Θ(nLogn).
