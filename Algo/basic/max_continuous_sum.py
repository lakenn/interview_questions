# from typing import List
#
#
# class Solution:
#     def largestContiguousSum(self, arr: List[int]) -> int:
#         # add your logic here
#         max_sum = float('-inf')
#         current_sum = 0
#
#         for num in arr:
#             current_sum = max(num, current_sum + num)
#             max_sum = max(max_sum, current_sum)
#
#         return max_sum
#
#         max_so_far = float('-inf')
#         max_ending_here = 0
#         for i in range(len(arr)):
#             max_ending_here = max_ending_here + arr[i]
#             if max_so_far < max_ending_here:
#                 max_so_far = max_ending_here
#             if max_ending_here < 0:
#                 max_ending_here = 0
#         return max_so_far
#
#
# a = Solution().largestContiguousSum([-2, -3, 4, -1, -2, 1, 5, -3])
# print(a)

import sys
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #         maxSum = prevMax = nums[0]

        #         for num in nums[1:]:
        #             currMax = max(prevMax + num, num)
        #             maxSum = max(currMax, maxSum)

        #             prevMax = currMax

        #         return maxSum

        #         window_sum = 0
        #         max_sum = -sys.maxsize

        #         for num in nums:
        #             window_sum += num

        #             window_sum = max(window_sum, num)
        #             max_sum = max(max_sum, window_sum)

        #         return max_sum

        max_sum = -sys.maxsize
        prev_sum = 0
        for num in nums:
            curr_sum = max(num, num + prev_sum)
            max_sum = max(max_sum, curr_sum)
            prev_sum = curr_sum

        return max_sum


