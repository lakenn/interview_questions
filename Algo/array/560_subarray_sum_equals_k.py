"""
560. Subarray Sum Equals K
Solved
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

# https://algo.monster/liteproblems/523
# https://www.aspires.cc/prefix-sum/

from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # currSum = 0
        # total = 0

        # prefixSumFreq = {0: 1}

        # for num in nums:
        #     currSum += num
        #     require_prefix_sum = currSum - k
        #     total += prefixSumFreq.get(require_prefix_sum, 0)
        #     prefixSumFreq[currSum] = prefixSumFreq.get(currSum, 0) + 1

        # return total
        cursum = 0
        res = 0
        prefix_sum_freq = defaultdict(int)
        prefix_sum_freq[0] = 1

        for num in nums:
            cursum += num
            compliment = cursum - k
            res += prefix_sum_freq[compliment]
            prefix_sum_freq[compliment] += 1

        return res

print(Solution().subarraySum([1,1,1], 2))