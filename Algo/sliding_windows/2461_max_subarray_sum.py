from collections import Counter
from typing import List

"""
2461. Maximum Sum of Distinct Subarrays With Length K
Solved
Medium
Topics
Companies
Hint
You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.
"""
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        num_cnt = Counter(nums[:k])
        curr_sum = sum(nums[:k])
        max_sum = curr_sum if len(num_cnt) == k else 0  # we have k distinct nums:

        # slide right one at a time
        for i in range(k, len(nums)):
            curr_sum += nums[i]
            curr_sum -= nums[i - k]
            num_cnt[nums[i]] += 1
            num_cnt[nums[i - k]] -= 1

            if num_cnt[nums[i - k]] == 0:
                del num_cnt[nums[i - k]]

            # only update max_sum if elems in subarray is all distinct
            if len(num_cnt) == k:
                max_sum = max(max_sum, curr_sum)

        return max_sum

nums = [1,5,4,2,9,9,9]

ans = Solution().maximumSubarraySum(nums, 3)
print(ans)
