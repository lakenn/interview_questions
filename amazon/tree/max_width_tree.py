class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return '%s' % self.value

max_left = 0
max_right = 0

def max_width_util(node, level):
    global max_left, max_right

    if node is None:
        return

    if level < max_left:
        max_left = level

    if level > max_right:
        max_right = level

    max_width_util(node.left, level - 1)
    max_width_util(node.right, level + 1)


def max_width(root):
    global max_left, max_right
    max_width_util(root, 0)

    return max_right - max_left

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print(max_width(root))