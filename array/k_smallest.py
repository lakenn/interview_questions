def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def partition(arr, start, end):
    pivot = arr[end]

    wall = start

    for idx in range(start, end):
        if arr[idx] <= pivot:
            swap(arr, wall, idx)
            wall +=1

    # put the pivot to the right side of the wall
    swap(arr, wall, end)
    # return sorted index of the pivot
    return wall

def quickSort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        quickSort(arr, start, pivot - 1 )
        quickSort(arr, pivot + 1, end)

def kthSmallest(arr, k):
    arr.sort()

    return arr[k-1]

# Driver code
if __name__=='__main__':
    arr = [12, 3, 5, 7, 19]
    k = 2
    print("K'th smallest element is",
          kthSmallest(arr, k))


    arr = [3, 5, 7, 12, 19]
    quickSort(arr, 0, len(arr) - 1)
    print(arr)