# https://leetcode.com/problems/minimum-path-sum/
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        for j in range(1, n):
            grid[0][j] += grid[0][j-1]

        for i in range(1, m):
            grid[i][0] += grid[i-1][0]

        for i in range(1, m):
            for j in range(1, n):
                # at i, j , two possible paths (from up or left)
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[m-1][n-1]

