#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'createBST' function below.
#
# The function accepts INTEGER_ARRAY keys as parameter.
#

counter = 0


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return '%s' % self.value


def binary_insert(root, node):
    global counter
    counter += 1

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


def createBST(keys):
    # Write your code here
    global counter
    root = None

    for key in keys:
        if root is None:
            root = Node(key)
        else:
            binary_insert(root, Node(key))

        print(counter)


if __name__ == '__main__':
    keys_count = int(input().strip())

    keys = []

    for _ in range(keys_count):
        keys_item = int(input().strip())
        keys.append(keys_item)

    createBST(keys)
