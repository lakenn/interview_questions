# https://algo.monster/problems/visible_tree_node

# In a binary tree, a node is labeled as "visible" if, on the path from the root to that node, there isn't any node with a value higher than this node's value.
#
# The root is always "visible" since there are no other nodes between the root and itself. Given a binary tree, count the number of "visible" nodes.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def visible_tree_node(root: Node) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    # preorder
    def dfs(root, max_so_far):
        if not root:
            return 0

        total = 0
        if root.val >= max_so_far:
            total += 1

        total += dfs(root.left, max(root.val, max_so_far))
        total += dfs(root.right, max(root.val, max_so_far))

        return total

    return dfs(root, -float('inf'))

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    # root = build_tree(iter(input().split()), int)
    nodes_input = iter(['5', '3', '2', 'x', 'x', '4', 'x', 'x', '7', '6', 'x', 'x', '8', 'x', 'x'])
    root = build_tree(nodes_input, int)
    res = visible_tree_node(root)
    print(res)