class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return '%s' % self.value


root = Node(1)
root.left = Node(2)
root.right = Node(3)


def reverse_tree(node):
    if node is None:
        return

    reversed_right = reverse_tree(node.right)
    reversed_left = reverse_tree(node.left)
    node.left = reversed_right
    node.right = reversed_left

    return node

reverse_tree(root)
print(1)