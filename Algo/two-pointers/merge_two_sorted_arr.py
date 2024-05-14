def merge_sorted_arr_with_extra_space(arr1, arr2):
    n1, n2 = len(arr1), len(arr2)
    sorted_arr = [None] * (n1 + n2)

    i, j, k = 0
    while i < n1 and j < n2:
        if arr1[i] > arr2[j]:
            sorted_arr[k] = arr2[j]
            j += 1
        else:
            sorted_arr[k] = arr1[i]
            i += 1
        k += 1

    while i < n1:
        sorted_arr[k] = arr1[i]
        i += 1
        k += 1

    while j < n2:
        sorted_arr[k] = arr2[j]
        j += 1
        k += 1

    return sorted_arr

def merge(nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m - 1] >= nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]

arr1 = [1, 5, 9, 10, 15, 20]
arr2 = [2, 3, 8, 13]

merge(arr1, len(arr1), arr2, len(arr2))