# Time Complexity:
"""
T(n) = T(n/2) + c
O(1) in case of iterative implementation.
In case of recursive implementation, O(Logn) recursion call stack space. (Theta(Logn))
"""


# Iterative implementation of Binary Search:
def binary_search(arr, item):
    high = len(arr) - 1
    low = 0

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return -1


arr = [1, 2, 15, 14, 5, 6, 10, 11, 12]
arr.sort()

print("Sorted Array : ", end=" ")
for i in range(0, len(arr)):
    print(arr[i], end=" ")
print()

item = 10

result = binary_search(arr, item)

if result == -1:
    print(item, "is not present in array")
else:
    print(item, "is present at index", result, "position", result+1)
print()


# Recursive implementation of Binary Search
def binary_search(arr, low, high, item):

    if high >= low:
        mid = low + (high - low) // 2

        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            return binary_search(arr, low, mid-1, item)
        else:

            return binary_search(arr, mid+1, high, item)
    else:
        return -1


arr = [1, 2, 15, 14, 5, 6, 10, 11]
arr.sort()
item = 10

result = binary_search(arr, 0, len(arr)-1, item)

if result == -1:
    print(item, "is not present in array")
else:
    print(item, "is present at index", result, "position", result+1)
print()


# Binary Search a String:
def binary_search(arr, item):
    high = len(arr)
    low = 0

    while low <= high:
        mid = low + (high - low) // 2

        res = item == arr[mid]

        if res == 0:
            return mid - 1
        elif res > 0:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# Driver Code:
if __name__ == "__main__":
    arr = ["contribute", "geeks", "ide", "practice"]
    item = "ide"
    result = binary_search(arr, item)

    if result == -1:
        print(item, "is not present in array")
    else:
        print(item, "is present at index", result, "position", result+1)

# the time complexity of Binary Search is log2 (n)
