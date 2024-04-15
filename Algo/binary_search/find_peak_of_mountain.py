# https://algo.monster/problems/peak_of_mountain_array

from typing import List

arr = [0, 1, 2, 3, 2, 1, 0]

def peak_of_mountain_array(arr: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE

    left, right = 0, len(arr)-1
    end = len(arr) -1

    while left <= right:
        mid = (left + right)//2

        if mid == end or arr[mid] > arr[mid+1]:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans

arr = [1,2,1,3,5,6,4]
print(peak_of_mountain_array(arr))