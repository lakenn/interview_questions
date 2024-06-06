# https://leetcode.com/problems/insert-interval/description/
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        result = []
        idx = 0

        # interval which is the left of newInterval
        while idx < n and newInterval[0] > intervals[idx][1]:
            result.append(intervals[idx])
            idx += 1

        # merge interval
        while idx < n and newInterval[1] >= intervals[idx][0]:
            newInterval[0] = min(newInterval[0], intervals[idx][0])
            newInterval[1] = max(newInterval[1], intervals[idx][1])
            idx += 1

        result.append(newInterval)

        # add reminaing of the interval which is right of the newInterval
        while idx < n:
            result.append(intervals[idx])
            idx += 1

        return result

