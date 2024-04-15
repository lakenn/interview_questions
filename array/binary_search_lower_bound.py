# function to find first index >= x
arr = [1, 2, 3, 5, 5, 6, 9]
def lower_index(arr, n, x):
    low = 0
    high = n-1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= x:
            high = mid - 1
        else:
            low = mid + 1

    return low



print(lower_index(arr, len(arr), 5))