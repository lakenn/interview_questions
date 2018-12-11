class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# top down
def reverse_tree(node):

    if node is None:
        return

    temp = node.left
    node.left = node.right
    node.right = temp

    reverse_tree(node.left)
    reverse_tree(node.right)


# bottom up (backtracking)
def reverse_tree_backtracking(node):

    if node is None:
        return

