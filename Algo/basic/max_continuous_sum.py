from typing import List


class Solution:
    def largestContiguousSum(self, arr: List[int]) -> int:
        # add your logic here
        max_sum = float('-inf')
        current_sum = 0

        for num in arr:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum

        max_so_far = float('-inf')
        max_ending_here = 0
        for i in range(len(arr)):
            max_ending_here = max_ending_here + arr[i]
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far


a = Solution().largestContiguousSum([-2, -3, 4, -1, -2, 1, 5, -3])
print(a)