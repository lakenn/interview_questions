def find_water(arr):
    length = len(arr)

    left = [0] * length
    right = [0] * length

    water = 0

    left[0] = arr[0]
    for i in range(1, length):
        left[i] = max(left[i - 1], arr[i])

    right[length-1] = arr[length - 1]
    for i in range(length -2, -1, -1):
        right[i] = max(right[i+1], arr[i])

    print(left)

# arr = [3, 0, 0, 2, 0, 4]
# find_water(arr)


def binsearch_adding_rank(A, v):
    l, u = 0, len(A)-1
    m=0
    while l <= u:
        m = l+(u-l)//2
        if v + m >= A[m]:
            l = m+1
            m+=1
            # We're binary searching for partitions, so if the last step was to the right
            # then add one to account for offset because that's where our insert would be.
        elif v+m < A[m]:
            u = m-1
    return v+m

print(binsearch_adding_rank([1, 5, 7], 2))