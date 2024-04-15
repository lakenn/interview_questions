from typing import List
import collections

# https://walkccc.me/LeetCode/problems/560/#__tabbed_1_2
# https://www.youtube.com/watch?v=fFVZt-6sgyo&ab_channel=NeetCode

class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:
        ...
        # prefix sum map with value = number of occurence of such prefix in current subarray

    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     ans = 0
    #     prefix = 0
    #     count = collections.Counter({0: 1})
    #
    #     for num in nums:
    #         prefix += num
    #         ans += count[prefix - k]
    #         count[prefix] += 1
    #
    #     return ans


# print(Solution().subarraySum([1,1,1,1], 2))
# print(Solution().subarraySum([1], 0))
print(Solution().subarraySum([1, 1, 1, 0, 1, 2], 3))
print(Solution().subarraySum([1, 2, 3], 3))