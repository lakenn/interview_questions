# https://www.aspires.cc/prefix-sum/


"""
523. Continuous Subarray Sum
Solved
Medium
Topics
Companies
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

"""
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # prefix sum technique
        # use a hashmap to store the prefix sum remainder found so far

        # edge case:
        # cumulative sum itself is a multiple of k from the beginning of the array
        cumsum = 0
        prefix_sum_remainder_map = {0: -1}

        for idx, num in enumerate(nums):
            cumsum += num
            remainder = cumsum % k

            if remainder in prefix_sum_remainder_map:
                if idx - prefix_sum_remainder_map.get(remainder) >= 2:
                    return True
            else:
                prefix_sum_remainder_map[remainder] = idx

        return False


