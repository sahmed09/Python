def linear_search(arr, x):
    for i in range(0, len(arr)):
        if arr[i] == x:
            return i
    return -1


# Driver code:
arr = [2, 3, 4, 10, 14]
x = 14
result = linear_search(arr, x)
if result == -1:
    print(x, "is not present in array")
else:
    print(x, "is present at index", result, "position", result+1)

# The time complexity of above algorithm is O(n)

