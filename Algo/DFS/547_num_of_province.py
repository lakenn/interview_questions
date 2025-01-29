from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cnt = 0
        visited = set()
        N = len(isConnected)

        def dfs(city):
            for neighbour in range(N):
                if isConnected[city][neighbour] and neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour)

        for city in range(N):
            if city not in visited:
                cnt += 1
                dfs(city)

        return cnt
