"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == []:
            return root

        current_level = []
        current_level.append(root)

        while current_level:
            next_node = None
            next_level = []

            for idx in range(len(current_level)):
                curr_node = current_level[idx]
                curr_node.next = next_node
                next_node = curr_node
                next_level.append(curr_node.right)
                next_level.append(curr_node.left)

            curr_level = next_level
            next_level = []

        return root

Solution().connect()