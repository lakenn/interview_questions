# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/description/
# https://walkccc.me/LeetCode/problems/1749/

"""
You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:

If x is a negative integer, then abs(x) = -x.
If x is a non-negative integer, then abs(x) = x.
"""


# https://usaco.guide/silver/more-prefix-sums?lang=cpp



class Solution:
  def maxAbsoluteSum(self, nums):
    summ = 0
    maxPrefix = 0
    minPrefix = 0

    max_prefix_arr = []
    min_prefix_arr = []
    for num in nums:
      summ += num
      maxPrefix = max(maxPrefix, summ)
      minPrefix = min(minPrefix, summ)

      max_prefix_arr.append(maxPrefix)
      min_prefix_arr.append(minPrefix)
    return maxPrefix - minPrefix

def maxSubarraySum(nums):
    prefix_sum = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
      prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

    max_sum = float('-inf')
    min_prefix_sum = 0
    for i in range(1, len(prefix_sum)):
        # max subarray sum is the maximum difference between two prefix sums
        max_sum = max(max_sum, prefix_sum[i] - min_prefix_sum)
        min_prefix_sum = min(min_prefix_sum, prefix_sum[i])

    summ = 0
    maxPrefix = 0
    minPrefix = 0

    max_prefix_arr = []
    min_prefix_arr = []
    for num in nums:
      summ += num
      maxPrefix = max(maxPrefix, summ)
      minPrefix = min(minPrefix, summ)

      max_prefix_arr.append(maxPrefix)
      min_prefix_arr.append(minPrefix)

    return max_sum


# Example usage:
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# maxSubarraySum(nums)
# print(maxSubarraySum(nums))  # Output: 6 (corresponding to [4, -1, 2, 1])
#
# class Solution:
#   def maxAbsoluteSum(self, nums):
#     ans = -math.inf
#     maxSum = 0
#     minSum = 0
#
#     for num in nums:
#       maxSum = max(num, maxSum + num)
#       minSum = min(num, minSum + num)
#       ans = max(ans, maxSum, -minSum)
#
#     return ans

Solution().maxAbsoluteSum([-3,-3,2,3,-4])
maxSubarraySum([-3,-3,2,3,-4])
print(Solution().maxAbsoluteSum([-2, -3, 4, -1, -2, 1, 5, -3]))