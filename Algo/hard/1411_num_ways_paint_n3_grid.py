# https://algo.monster/liteproblems/1411
# https://github.com/doocs/leetcode/blob/main/solution/1400-1499/1411.Number%20of%20Ways%20to%20Paint%20N%20%C3%97%203%20Grid/README_EN.md

"""
1411. Number of Ways to Paint N × 3 Grid
Hard
Topics
Companies
Hint
You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors: Red, Yellow, or Green while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).

Given n the number of rows of the grid, return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 109 + 7.


Input: n = 1
Output: 12
Explanation: There are 12 possible way to paint the grid as shown.
Example 2:

Input: n = 5000
Output: 30228214
"""