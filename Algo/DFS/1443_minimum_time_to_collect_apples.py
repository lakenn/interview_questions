# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/description/

"""
1443. Minimum Time to Collect All Apples in a Tree
Medium
Topics
Companies
Hint
Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend to collect all apples in the tree, starting at vertex 0 and coming back to this vertex.

The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi. Additionally, there is a boolean array hasApple, where hasApple[i] = true means that vertex i has an apple; otherwise, it does not have any apple.

"""
from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # build adj list
        graph = [[] for _ in range(n)]

        for idx, (start, end) in enumerate(edges):
            graph[start].append(end)
        def max_value(node_id):
            if graph[node_id] == []:
                return 2 if hasApple[node_id] else 0

            # dfs child node
            child_time = sum([max_value(child_node) for child_node in graph[node_id]])
            if node_id == 0:
                return child_time

            if hasApple[node_id] or child_time > 0:
                return child_time + 2
            else:
                return 0

        return max_value(0)

print(Solution().minTime(4, [[0,2],[0,3],[1,2]], [False,True,False,False]))