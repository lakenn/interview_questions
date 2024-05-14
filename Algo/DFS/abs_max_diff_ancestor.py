# https://walkccc.me/LeetCode/problems/1026/
# https://leetcode.ca/2018-09-21-1026-Maximum-Difference-Between-Node-and-Ancestor/

def dfs(node, min_val, max_val):

    if node == None:
        return 0

    min_val = min(node.val, min_val)
    max_val = max(node.val, max_val)

    left_ans = dfs(node.left, min_val, max_val)
    right_ans = dfs(node.right, min_val, max_val)

    return max(max_val - min_val, left_ans, right_ans)