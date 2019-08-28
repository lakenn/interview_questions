# !/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'teamFormation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY score
#  2. INTEGER team
#  3. INTEGER m
#
import heapq

class MyPriorityQueue:
    def __init__(self):
        self.queue = []

    def top(self):
        return self.queue[0]

    def push(self, val):
        heapq.heappush(self.queue, val)

    def pop(self):
        return heapq.heappop(self.queue)


def teamFormation(score, team, m):
    # Write your code here
    lpq = MyPriorityQueue()
    rpq = MyPriorityQueue()

    n = len(score)
    left = 0
    right = n - 1


    while left < m:
        lpq.push(-score[left])
        left += 1

    while right >= n - m:
        rpq.push(-score[right])
        right -= 1

    i = 0
    max_score = 0

    while i < team:
        if len(lpq.queue) and len(rpq.queue):
            if lpq.top() <= rpq.top():
                val = -lpq.pop()
                max_score += val
                pq = 1
            else:
                val = -rpq.pop()
                max_score += val
                pq = 2

            if not left > right :
                if pq == 1:
                    lpq.push(-score[left])
                    left += 1
                else:
                    rpq.push(-score[right])
                    right -= 1
        else:
            # exhausted
            if len(lpq.queue):
                max_score += -lpq.pop()
            else:
                max_score += -rpq.pop()

        i += 1

    return max_score


if __name__ == '__main__':
    #score = [17, 12, 10, 2, 7, 2, 11, 20,8]
    score = [6, 18, 8, 14, 10, 12, 18, 9]
    score = [6, 18, 8]
    print(teamFormation(score, 3, 3))
