"""
https://leetcode.com/problems/merge-intervals/description/
"""

"""


Code

Testcase

Test Result
Test Result
56. Merge Intervals
Medium

Topics
Companies
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

"""
from typing import List


class Solution:
    def mergeIntervals(self, intervals: List[List[int]]) -> List[List[int]]:
        # add your logic here

        intervals.sort(key=lambda x: (x[0], x[1]))
        res = [intervals[0]]

        for idx in range(1, len(intervals)):
            interval = intervals[idx]
            if res[-1][1] > interval[0]:
                if res[-1][1] < interval[1]:
                    res[-1] = (res[-1][0], interval[1])
            else:
                res.append(interval)

        return res



print(Solution().mergeIntervals([[1, 1], [2, 2], [3, 3]]))