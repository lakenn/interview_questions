# https://algo.monster/problems/peak_of_mountain_array

from typing import List

arr = [0, 1, 2, 3, 2, 1, 0]

#The array strictly increases until the peak element and then strictly decreases.
# The monotonicity is a strong sign that we can use binary search to find the peak element.

def peak_of_mountain_array(arr: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE

    left, right = 0, len(arr)-1
    end = len(arr) -1

    while left <= right:
        mid = (left + right)//2

        # maybe the peak and keep looking left of mid
        if mid == end or arr[mid] > arr[mid+1]:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans

arr = [1,2,1,3,5,6,4]
print(peak_of_mountain_array(arr))