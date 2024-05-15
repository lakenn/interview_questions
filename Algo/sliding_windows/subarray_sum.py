from typing import List
import collections

# https://walkccc.me/LeetCode/problems/560/#__tabbed_1_2
# https://www.youtube.com/watch?v=fFVZt-6sgyo&ab_channel=NeetCode

# *positive*
# can't use the sliding/stretching window technique when there are negative numbers in the array, because the sum doesn't grow monotonically with the window size.

"""
560. Subarray Sum Equals K
Medium

Topics
Companies

Hint
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
"""

#   prefixsum

class Solution:
  def subarraySum(self, nums: List[int], k: int) -> int:
    ans = 0
    prefix = 0
    count = collections.Counter({0: 1})

    for num in nums:
      prefix += num
      ans += count[prefix - k]
      count[prefix] += 1

    return ans

# print(Solution().subarraySum([1,1,1,1], 2))
# print(Solution().subarraySum([1], 0))
print(Solution().subarraySum([1, 1, 1, 0, 1, 2], 3))
print(Solution().subarraySum([1, 2, 3], 3))