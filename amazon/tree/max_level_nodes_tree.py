# Python program to find the maximum width of binary tree using Preorder Traversal.

# A binary tree node
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to get the maximum width of a binary tree
def getMaxWidth(root):
    h = height(root)
    # Create an array that will store count of nodes at each level
    count = [0] * h

    level = 0
    # Fill the count array using preorder traversal
    getMaxWidthRecur(root, count, level)

    # Return the maximum value from count array
    return getMax(count, h)


# A function that fills count array with count of nodes at every
# level of given binary tree
def getMaxWidthRecur(root, count, level):
    if root is not None:
        count[level] += 1
        getMaxWidthRecur(root.left, count, level + 1)
        getMaxWidthRecur(root.right, count, level + 1)

        # UTILITY FUNCTIONS


# Compute the "height" of a tree -- the number of
# nodes along the longest path from the root node
# down to the farthest leaf node.
def height(node):
    if node is None:
        return 0
    else:
        # compute the height of each subtree
        lHeight = height(node.left)
        rHeight = height(node.right)
        # use the larger one
        return (lHeight + 1) if (lHeight > rHeight) else (rHeight + 1)

        # Return the maximum value from count array


def getMax(count, n):
    max = count[0]
    for i in range(1, n):
        if (count[i] > max):
            max = count[i]
    return max


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(8)
root.right.right.left = Node(6)
root.right.right.right = Node(7)

""" 
Constructed bunary tree is: 
       1 
      / \ 
     2   3 
    / \      \ 
   4   5   8  
          / \ 
         6   7 
"""
getMaxWidth(root)