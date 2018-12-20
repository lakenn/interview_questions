# arr = [-10, -9, -8, 0, 1, 2, 3]

def max_product(arr, k):
    arr.sort()

    # two pointers
    count = 0
    result = 1

    low = -1
    high = len(arr)
    while count < k:

        if abs(arr[low+1]) < abs(arr[high-1]):
            larger = arr[high-1]
            high -= 1
        else:
            larger = arr[low+1]
            low += 1

        result *= larger
        count += 1

    if result > 0:
        return result
    else:
        # result is negative, try to find a better solution by moving the window
        if arr[low]*arr[low+1] < arr[high]*arr[high-1]:
            result = int(result / arr[low]) * arr[high - 1]
            low -= 1
            high -= 1

        else:
            result = int(result / arr[high]) * arr[low + 1]
            low += 1
            high += 1

        return result, low, high

arr= [-6, -4, -2, -1, 2, 3, 10]
result, low, high = max_product(arr, 6)
print(result, low, high)
