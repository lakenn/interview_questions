from typing import List

# https://algo.monster/liteproblems/2099
# https://walkccc.me/LeetCode/problems/2099/#__tabbed_1_3

class Solution:
  def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
    ans = []
    threshold = sorted(nums)[-k]
    larger = sum(num > threshold for num in nums)
    equal = k - larger

    for num in nums:
      if num > threshold:
        ans.append(num)
      elif num == threshold and equal:
        ans.append(num)
        equal -= 1

    return ans

Solution().maxSubsequence([2,2, 2, 2 ,2, 3] , 3)