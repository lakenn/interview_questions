from itertools import accumulate
from typing import List

# https://algo.monster/liteproblems/303

class NumArray:
    def __init__(self, nums: List[int]):
        # Pre-calculate the cumulative sum of the array.
        # The 'initial=0' makes sure the sum starts from index 0 for easier calculations.
        self.cumulative_sum = list(accumulate(nums, initial=0))

    def sumRange(self, left: int, right: int) -> int:
        # Calculate the sum of elements between 'left' and 'right'
        # by subtracting the sum up to 'left' from the sum up to 'right + 1'.
        return self.cumulative_sum[right + 1] - self.cumulative_sum[left]


class NumArray:

    def __init__(self, nums: list[int]):
        # Build prefix sum array
        self.prefix_sum = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        # Sum range between indices left and right
        return self.prefix_sum[right + 1] - self.prefix_sum[left]

# Example usage:
nums = [-2, 0, 3, -5, 2, -1]
num_array = NumArray(nums)
print(num_array.sumRange(0, 2))  # Output: 1 (sum of nums[0:3] => -2 + 0 + 3)
print(num_array.sumRange(2, 5))  # Output: 3 (sum of nums[2:6] => 3 - 5 + 2 - 1)
print(num_array.sumRange(0, 5))  # Output: -3 (sum of nums[0:6] => -2 + 0 + 3 - 5 + 2 - 1)
