# https://leetcode.com/problems/time-needed-to-inform-all-employees/
from typing import List

"""1376. Time Needed to Inform All Employees
Solved
Medium
Topics
Companies
Hint
A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.

Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the urgent news.

 

Example 1:

Input: n = 1, headID = 0, manager = [-1], informTime = [0]
Output: 0
Explanation: The head of the company is the only employee in the company.
"""

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # n = 7
        # headId = 6
        # manager = [1,2,3,4,5,6,-1]
        # informTime = [0,6,5,4,3,2,1]
        root_index = manager.index(-1)

        reach_time = [-1] * n

        max_reach_time = 0

        def find_max_reach_time(index):
            if reach_time[index] != -1:
                return reach_time[index]

            # reach the top
            if manager[index] == -1:
                return 0

            reach_time[index] = informTime[manager[index]] + find_max_reach_time(manager[index])
            return reach_time[index]

        for i in range(n):
            if informTime[i] == 0:  # it is a leaf node
                max_reach_time = max(max_reach_time, find_max_reach_time(i))

        return max_reach_time