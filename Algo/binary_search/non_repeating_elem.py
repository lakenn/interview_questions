# https://workat.tech/problem-solving/approach/nre/non-repeating-element

arr = [1, 1, 2, 3, 3, 4, 4]

def find_non_repeating_element(arr):
    left, right = 0, len(arr)-1

    while left <= right:
        mid = (left + right)//2

        if left == right:
            return arr[mid]

        if mid % 2 == 0:
            if arr[mid] == arr[mid+1]:
                left = mid + 1
            else:
                right = mid -1
        else:
            if arr[mid] == arr[mid-1]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

print(find_non_repeating_element(arr))