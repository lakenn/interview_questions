from typing import List


def find_last_occurrence(arr: List[int], target: int) -> int:
    left, right = 0, len(arr)-1
    ans = -1

    while left <= right:
        mid = (left + right)//2

        if arr[mid] > target:
            # we need to search from the left of mid
            right = mid - 1

        elif arr[mid] == target:
            # continue to find right of the mid
            left = mid + 1
            ans = mid
        else:
            left = mid + 1

    return ans


print(find_last_occurrence([1,2,3,4,5,6,7,7, 8,9,9,9], 9))

# 9 ->3
# 8 -> 2.xxx
#The right variable always holds the last valid mid where mid * mid ≤ x.
# When the loop exits, left has gone beyond the valid square root, so returning right gives us the correct floor value.
def find_sqrt(x):
    if x < 0:
        raise ValueError('sqrt of negative number is not defined')

    left, right = 0, x//2

    while left <= right:
        mid = (left + right) // 2

        if mid * mid == x:
            return mid

        if mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1

    return right


def find_first_occurrence(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    ans = -1

    while left <= right:
        mid = (left + right)//2

        if arr[mid] == target:
            right = mid - 1
            ans = mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return ans

print(find_first_occurrence([1,2,3,4,5,6,7,7, 8,9,9,9], 9))