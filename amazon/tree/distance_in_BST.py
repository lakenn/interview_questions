class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return '%s' % self.value


def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.value > node.value:
            if root.left is None:
                root.left = node
            else:
                binary_insert(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                binary_insert(root.right, node)


def lca(root, node1, node2):
    if root is None:
        return None

    if root.value > node1 and root.value > node2:
        return lca(root.left, node1, node2)

    if root.value < node1 and root.value < node2:
        return lca(root.right, node1, node2)

    return root


def distance_from_root(root, node):
    if root.value == node:
        return 0
    elif root.value > node:
        return 1 + distance_from_root(root.left, node)
    else:
        return 1 + distance_from_root(root.right, node)


def distance(root, node1, node2):
    if root.value > node1 and root.value > node2:
        return distance(root.left, node1, node2)

    if root.value < node1 and root.value < node2:
        return distance(root.right, node1, node2)

    if root.value >= node1 and root.value <= node2:
        return distance_from_root(root, node1) + distance_from_root(root, node2)


def bstDistance(values, n, node1, node2):
    # WRITE YOUR CODE HERE

    if node1 not in values or node2 not in values:
        return -1

    # build BST
    if n >= 1:
        root = Node(values[0])

        for i in range(1, n):
            binary_insert(root, Node(values[i]))

        if node1 > node2:
            return distance(root, node2, node1)

        return distance(root, node1, node2)
    else:
        return -1


bstDistance([5, 6, 3, 1, 2, 4], 6,2,4)
#3

#[9,7,5,3,1], 5, 7, 20
#-1