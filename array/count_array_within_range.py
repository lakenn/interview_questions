'''
Queries for counts of array elements with values in given range

'''

arr = [1, 4, 8, 3, 4, 9, 10, 3]

# queries
i = 11
j = 12

def solution(arr, i, j):
    count = 0

    for elem in arr:
        if elem >= i and elem <= j:
            count += 1

    return count


print(solution(arr, i, j))


# using modified binary search
# function to find first lower index >= x

def lower_index(arr, i):
    l = 0
    h = len(arr) - 1

    while(l <= h):
        mid = (l + h) // 2
        if arr[mid] >= i:
            h = mid - 1
        else:
            # mid is smaller than x, so move l to mid + 1
            l = mid + 1

    return l

def upper_index(arr, j):
    l = 0
    h = len(arr) - 1

    while(l <= h):
        mid = (l + h) // 2
        if arr[mid] <= j:
            l = mid + 1
        else:
            h = mid - 1

    return h

arr.sort()
lower = lower_index(arr, i)
upper = upper_index(arr, j)
print(upper-lower+1)