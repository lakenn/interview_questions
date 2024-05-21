from typing import List

# https://leetcode.com/problems/number-of-islands/submissions/

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        def bucketFill(j, i, grid, visited):
            if i < 0 or j < 0 or i >= len(grid[0]) or j >= len(grid):
                return

            if visited[j][i] or grid[j][i] == '0':
                return

            visited[j][i] = 1

            bucketFill(j+1, i, grid, visited)
            bucketFill(j, i+1, grid, visited)
            bucketFill(j-1, i, grid, visited)
            bucketFill(j, i-1, grid, visited)

        ans = 0
        # create a visited grid
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]

        # scan thru the grid
        for j in range(len(grid)):
            for i in range(len(grid[0])):
                if grid[j][i] == '1' and not visited[j][i]:
                    ans += 1
                    bucketFill(j, i, grid, visited)

        return ans

grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]


grid = [
        ["0","1","0"],
        ["1","0","1"],
        ["0","1","0"]
]

grid = [
    ["1","1","1"],
    ["0","1","0"],
    ["1","1","1"]
]

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
sol = Solution()
ans = sol.numIslands(grid)
print(ans)