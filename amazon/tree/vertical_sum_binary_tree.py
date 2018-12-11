class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return '%s' % self.value

def vertical_sum_util(node, level, smap):
    if node is None:
        return

    # push itself into the dict
    smap[level] = smap.get(level, 0) + node.value
    vertical_sum_util(node.left, level - 1, smap)
    vertical_sum_util(node.right, level + 1, smap)

def vertical_sum(root):
    if root is None:
        return

    smap = {}

    vertical_sum_util(root, 0, smap)

    print_order = list(smap.keys())
    print_order.sort()

    for idx in print_order:
        print('%s %s' % (idx, smap[idx]))


def vertical_sum_dll(root):
    pass

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    vertical_sum(root)