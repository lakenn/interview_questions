from typing import List


# https://prepfortech.io/leetcode-solutions/max-consecutive-ones-ii
# https://algo.monster/liteproblems/487
# https://medium.com/@timpark0807/leetcode-is-easy-sliding-window-c44c11cc33e1

"""
487. Max Consecutive Ones II
Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:

Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Initialize the left and right pointers
        left_pointer = right_pointer = 0
        zero_count = 1  # Variable to allow flipping of one '0' to '1'

        # Traverse the array while the right_pointer is within the array bounds
        while right_pointer < len(nums):
            # Decrease zero_count when a '0' is encountered
            if nums[right_pointer] == 0:
                zero_count -= 1

            # If zero_count is less than 0, slide the window to the right
            # by moving the left_pointer to the next position
            if zero_count < 0:
                # When we move the left_pointer forward, we need to check if
                # we are passing over a '0' and if so, increase zero_count
                if nums[left_pointer] == 0:
                    zero_count += 1
                # Move the left pointer to the right
                left_pointer += 1

            # Move the right pointer to the right
            right_pointer += 1

        # The length of the longest subarray of 1's (possibly with one flipped 0)
        # is the difference between the right and left pointers.
        return right_pointer - left_pointer
#                                                          *
print(Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1]))