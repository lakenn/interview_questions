# https://leetcode.com/problems/minimum-size-subarray-sum/description/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        window_sum = 0
        min_len = n + 1
        i = 0

        # sliding window technique
        for j in range(n):
            window_sum += nums[j]

            while window_sum >= target:
                min_len = min(min_len, j - i + 1)
                window_sum -= nums[i]
                i += 1

        return min_len if min_len != n + 1 else 0

        # binary search of right boundary of prefix_sum
        # prefix_sum[mid] - prefix_sum[i] = window sum between i+1 and mid
        # objective: find the right boundary of the prefix_sum with each index i
        # prefix_sum[mid] >= target + prefix_sum[i]
        # O(nlogn)
#         prefix_sum = [0] * (n+1)

#         for i in range(n):
#             prefix_sum[i+1] = prefix_sum[i] + nums[i]


#         for i in range(n):
#             t = prefix_sum[i] + target
#             left = i+1
#             right = n

#             while left <= right:
#                 mid = left + (right - left)//2

#                 if prefix_sum[mid] >= t:
#                     right = mid-1
#                 else:
#                     left = mid+1

#             # nth found -- whole array not satisfying condition:
#             if left == n+1:
#                 break

#             min_len = min(min_len, left-i)

#         return 0 if min_len == n+1 else min_len








