"""

The problem asks us to find the maximum length of a subarray from the given array nums, such that the sum of its elements is exactly equal to the given integer k. A subarray is a contiguous part of an array. If such a subarray doesn't exist, we should return 0.

To clarify with an example, let's say our array is [1, -1, 5, -2, 3] and k is 3.
The subarray [1, -1, 5, -2] sums to 3, and its length is 4,
which would be the answer because there's no longer subarray that sums to 3.

To approach this problem, we need to find a way to efficiently look up the sum of elements from the beginning of the array up to a certain point, and determine if there is a previous point where the sum was exactly k less than the current sum. If we can find such a place,
then the elements between these two points form a subarray that sums to k.
"""
from typing import List


# https://algo.monster/liteproblems/325

class Solution:
    def maxSubArrayLen(self, nums: List[int], target: int) -> int:
        prefix_sum_map = {0 : -1}
        max_length = cursum = 0

        for idx, num in enumerate(nums):
            cursum += num
            compliment = cursum - target

            if compliment in prefix_sum_map:
                max_length = max(max_length, idx - prefix_sum_map.get(compliment))

            if cursum not in prefix_sum_map:
                prefix_sum_map[cursum] = idx

        return max_length
