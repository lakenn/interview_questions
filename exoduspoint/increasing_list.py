#!/bin/python

import math
import os
import random
import re
import sys

"""
Problem Statement:
You are given a custom list, IncreasingList, that supports three operations: append, pop, and size.

append val: This operation inserts the value val into the list while ensuring that the list maintains an increasing order. 
Specifically, before adding the new element, it removes any elements in the list that are larger than val starting from the end of the list.

pop: This operation removes the last element of the list, if it is not empty. If the list is empty, it does nothing.

size: This operation outputs the current size of the list.

You will be given a series of operations in the form of a list of strings. For each operation, perform the corresponding action on the list.

Input Format:
The first line contains an integer q, the number of operations.
Each of the next q lines contains an operation in the form of a string, which could be one of the following:
append val: Insert val into the list maintaining the increasing order.
pop: Remove the last element from the list.
size: Print the current size of the list.
Output Format:
For every size operation, print the current size of the list.
"""
class IncList:
    def __init__(self):
        self.stack = []

    def append(self, val):
        """
        first, it removes all elements from the list from the end that have greater values than val, starting from the last one,
        and once there are no greater element in the list, it appends val to the end of the list
        """
        while self.stack and self.stack[-1] > val:
            self.stack.pop()

        self.stack.append(val)

    def pop(self):
        if self.stack:
            return self.stack.pop()

    def size(self):
        return len(self.stack)




if __name__ == '__main__':
    fptr = open('output.txt', 'w')
    lst = IncList()
    q = int(input())
    for _ in range(q):
        op = input().split()
        op_name = op[0]
        if op_name == "append":
            val = int(op[1])
            lst.append(val)
        elif op_name == "pop":
            lst.pop()
        elif op_name == "size":
            fptr.write("%d\n" % len(lst))
        else:
            raise ValueError("invalid operation")
    fptr.close()


class IncreasingList:
    def __init__(self):
        self.items = []


    def append(self, val):
        """
        First, it removes all elements from the list that have greater values than val,
        starting from the last one, and once there are no greater elements in the list,
        it appends val to the end of the list.
        """
        idx = len(self.stack) - 1
        while idx >= 0 and self.stack[idx] > val:
            self.stack.pop()
            idx -= 1

        self.stack.append(val)

    # def append(self, val):
    #     """
    #     first, it removes all elements from the list that have greater values than val, starting from the last one, and once there are no greater element in the list, it appends val to the end of the list
    #     """
    #     idx = 0
    #     for i in reversed(range(len(self))):
    #         idx = i
    #         if val >= self.items[idx]:
    #             break
    #
    #     self.items = self.items[:idx + 1] + [val]

    def pop(self):
        """
        removes the last element from the list if the list is not empty, otherwise, if the list is empty, it does nothing
        """
        if len(self):
            return self.items.pop(-1)

    def __len__(self):
        """
        returns the number of elements in the list
        """
        return len(self.items)


if __name__ == '__main__':
    fptr = open('output.txt', 'w')
    lst = IncreasingList()
    q = int(input())
    for _ in range(q):
        op = input().split()
        op_name = op[0]
        if op_name == "append":
            val = int(op[1])
            lst.append(val)
        elif op_name == "pop":
            lst.pop()
        elif op_name == "size":
            fptr.write("%d\n" % len(lst))
        else:
            raise ValueError("invalid operation")
    fptr.close()