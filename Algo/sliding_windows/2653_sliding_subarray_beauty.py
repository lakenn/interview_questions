# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

"""
2653. Sliding Subarray Beauty
Solved
Medium
Topics
Companies
Hint
Given an integer array nums containing n integers, find the beauty of each subarray of size k.

The beauty of a subarray is the xth smallest integer in the subarray if it is negative, or 0 if there are fewer than x negative integers.

Return an integer array containing n - k + 1 integers, which denote the beauty of the subarrays in order from the first index in the array.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,-1,-3,-2,3], k = 3, x = 2
Output: [-1,-2,-2]
Explanation: There are 3 subarrays with size k = 3.
The first subarray is [1, -1, -3] and the 2nd smallest negative integer is -1.
The second subarray is [-1, -3, -2] and the 2nd smallest negative integer is -2.
The third subarray is [-3, -2, 3] and the 2nd smallest negative integer is -2.
"""

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []
        count = [0] * 50  # count[i] := the frequency of (i + 50)

        for i, num in enumerate(nums):
            if num < 0:
                count[num + 50] += 1
            if i - k >= 0 and nums[i - k] < 0:
                count[nums[i - k] + 50] -= 1
            if i + 1 >= k:
                ans.append(self._getXthSmallestNum(count, x))

        return ans

    def _getXthSmallestNum(self, count: List[int], x: int) -> int:
        prefix = 0
        for i in range(50):
            prefix += count[i]
            if prefix >= x:
                return i - 50
        return 0