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