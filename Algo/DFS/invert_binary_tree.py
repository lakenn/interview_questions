# Definition for a binary tree node.
from typing import Optional
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         if root is None:
#             return
#
#         root.left, root.right = root.right, root.left
#         self.invertTree(root.left)
#         self.invertTree(root.right)
#
#         return root

def print_tree(root):
    if root:
        print(root.val)
        print_tree(root.left)
        print_tree(root.right)

def invert_tree(root):
    if root:
        root.right, root.left = invert_tree(root.left), invert_tree(root.right)
    return root

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Printing the original tree
print("Original tree:")
print_tree(root)

# Inverting the tree
inverted_root = invert_tree(root)

# Printing the inverted tree
print("\nInverted tree:")
print_tree(inverted_root)