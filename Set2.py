import random

class Node():
    def __init__(self, data):
        self.data = data
        self.height = None
        self.left = None
        self.right = None


def height(node):
    if node is None:
        return 0

    return max(height(node.left), height(node.right)) + 1

def is_balanced(node):
    # definition of height balanced:
    # abs(height(node.left) - height(node.right))  <= 1
        # height of a node:
        #   - The height of a node is the number of edges on the longest path between that node and a leaf
        #   - max(height(node.left), height(node.right)) + 1
    # is_balanced(node.left) and is_balanced(node.right)

    # base case
    if node is None:
        return True

    if abs(height(node.left) - height(node.right)) <= 1 and is_balanced(node.left) and is_balanced(node.right):
        return True

    return False

root = Node(1)
root.left = Node(2)

#print(height(root))
#print(is_balanced(root))


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)

root.right = Node(3)
root.right.right = Node(6)
root.right.right.right = Node(7)

def height_opt(node):
    if node is None:
        return 0

    return max(height(node.left), height(node.right)) + 1

def is_balanced_opt(node):

    if node is None:
        return True, 0

    ltree, ltree_height = is_balanced_opt(node.left)
    rtree, rtree_height = is_balanced_opt(node.right)

    # height of current node
    node.height = max(ltree_height, rtree_height) + 1

    if abs(ltree_height - rtree_height) <= 1 and ltree and rtree:
        return True, node.height

    return False, node.height

print(is_balanced_opt(root))


# A binary tree node
class Node:
    # constructor to create node of
    # binary tree
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# utility class to pass height object
class Height:
    def __init__(self):
        self.height = 0


# helper function to check if binary
# tree is height balanced
def isBalanced(root, height):
    # lh and rh to store height of
    # left and right subtree
    lh = Height()
    rh = Height()

    # Base condition when tree is
    # empty return true
    if root is None:
        return True

    # l and r are used to check if left
    # and right subtree are balanced
    l = isBalanced(root.left, lh)
    r = isBalanced(root.right, rh)

    # height of tree is maximum of
    # left subtree height and
    # right subtree height plus 1
    height.height = max(lh.height, rh.height) + 1

    if abs(lh.height - rh.height) <= 1:
        return l and r

    # if we reach here then the tree
    # is not balanced
    return False


height = Height()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.left.left.left = Node(7)

if isBalanced(root, height):
    print('Tree is balanced')
else:
    print('Tree is not balanced')

f = lambda x, y, z: x + y + z

def adder(x, y, z):
	return (x + y + z)

print(type(f))
print(type(adder))

names = ['Mary', 'Isla', 'Sam']

f2 = lambda x: random.choice(['Mr. Pink', 'Mr. Orange', 'Mr. Blonde'])

def f3(x):
    return random.choice(['Mr. Pink', 'Mr. Orange', 'Mr. Blonde'])

secret_names = map(f3, names)
print(list(secret_names))


def permutation(ans, choices, level, max_level):

    if level > max_level:
        print(ans)
        return

    for choice in choices:
        print(choice)
        ans.append(choice)
        permutation(ans, choices, level+1, max_level)
        ans.pop()


permutation([], ['a','b'], 1, 2)