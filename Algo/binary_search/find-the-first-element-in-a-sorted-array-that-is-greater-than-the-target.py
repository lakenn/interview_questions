# https://stackoverflow.com/questions/6553970/find-the-first-element-in-a-sorted-array-that-is-greater-than-the-target
from typing import List

# Any element to the right of the end is greater than the target.
# Any element to the left of the start is smaller than or equal to the target.

'''
With this invariant, when the loop finishes, the first element after the end will be the answer (remember the invariant that 
the right side of the end are all greater than the target?). So answer = end + 1.

Also, we need to note that when the loop finishes, the start will be one more than the end. ie start = end + 1. 
So equivalently we can say start is the answer as well (invariant was that anything to the left of the start is smaller than 
or equal to the target, so start itself is the first element larger than the target).
'''

def find_first_greater_than_target(nums, target):
    left = 0
    right = len(nums) - 1
    result_index = -1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] > target:
            result_index = mid  # Update result index to current mid
            right = mid - 1     # Search on the left half for a greater element
        else: # mid <= target
            left = mid + 1      # Search on the right half

    return result_index


def find_first_greater_than_target(arr: List[int], target: int) -> int:
    l, r = 0, len(arr) - 1

    while l <= r:
        mid = (l + r)//2

        # Any element to the left of the start is smaller than or equal to the target.
        if arr[mid] <= target:
            l = mid + 1
        else:   # mid > target
            r = mid - 1

    return l #  or return  r + 1

def find_first_less_than_target(arr: List[int], target: int) -> int:
    l, r = 0, len(arr) - 1
    result_index = -1

    while l <= r:
        mid = (l + r) // 2

        if arr[mid] < target:
            result_index = mid  # Update result index to current mid
            l = mid + 1         # Continue search on the right half for a greater element
        else:   # arr[mid] >= target
            r = mid - 1         # Continue search on the left half

    return result_index

def find_first_occurrence(arr: List[int], target: int) -> int:
    l, r = 0, len(arr)-1
    ans = -1

    while l <= r:
        mid = (l + r) // 2

        if arr[mid] == target:
            ans = mid
            r = mid - 1
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return ans
