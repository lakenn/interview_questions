# https://www.enjoyalgorithms.com/blog/validate-binary-search-tree
# https://dev.to/samuelhinchliffe/98-validate-binary-search-tree-1cc9

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_valid_bst(root):
    bst = True
    prev_node = TreeNode(float('-inf'))

    def in_order(root):
        nonlocal prev_node, bst
        if root is None or not bst:
            return

        in_order(root.left)
        if root.value <= prev_node.value:
            bst = False

        prev_node = root
        in_order(root.right)

    in_order(root)
    return bst

def is_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True

    if not min_val < root.value < max_val:
        return False

    return (is_bst(root.left, min_val, root.value) and
            is_bst(root.right, root.value, max_val))

# Example usage
# Assuming you already have a binary tree root node named 'root'

# if is_bst(root):
#     print("The tree is a Binary Search Tree.")
# else:
#     print("The tree is not a Binary Search Tree.")


def is_valid_bst(root):
    is_valid = True
    prev_node = TreeNode(float('-inf'))

    def in_order(root):
        nonlocal is_valid, prev_node
        if root is None or not is_valid:
            return

        in_order(root.left)
        if root.value <= prev_node.value:
            is_valid = False
            return
        prev_node = root
        in_order(root.right)

    in_order(root)
    return is_valid
