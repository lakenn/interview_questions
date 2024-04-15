# https://workat.tech/problem-solving/practice/sliding-window-maximum
# https://www.scaler.com/topics/sliding-window-maximum/
# https://www.interviewbit.com/blog/sliding-window-maximum/
from collections import deque
from typing import List


# You are given an array of integers A and a number k which represents the size of the window.
# The window covers k elements and starts at the left-end of the array.
# The window moves one index to the right at every step.
#
# You need to return an array with the max element inside the window at every step.

# A: [1, -2, 3, 4, 5, 3, 4, -1]
# k: 3
# Result: [3, 4, 5, 5, 5, 4]

from collections import deque


# Thinking:
1. I need a DS to remember the "max" seen so far when traversing thru the array
a. PriorityQueue
    - Head always give you the maximum value
    - however, we need to check the head is within window size or not (idx > i-K)

b. Deque
    - Deque[0] always give you the maximum value
    - we also need to check if head is within window size but don't need to use a while loop to check
    - To transform a simple doubly-ended queue into a monotonic doubly ended queue - Before we push x in the queue, we pop out all elements less than x".
def SlidingWindowMaximum(A, K):
    n = len(A)
    if n * K == 0:
        return []
    if K == 1:
        return A

    def clean_deque(i):
        if deq and deq[0] == i - K:
            deq.popleft()

        while deq and A[i] > A[deq[-1]]:
            deq.pop()

    deq = deque()
    for i in range(K):
        clean_deque(i)
        deq.append(i)
    output = [A[deq[0]]]

    for i in range(K, n):
        clean_deque(i)
        deq.append(i)
        output.append(A[deq[0]])
    return output

#                              0  1   2   3  4  5  6  7
print(SlidingWindowMaximum([1, 3, -1, -3, 5, 3, 6, 7], 3))


# def sliding_window_max(A, K):
#     # use deque to keep track of idx of the element such that it is a
#     # monotonic decreasing doubly ended queue
#     window = deque()
#
#     def clean_deque(i):
#         # remove leftmost element that are out of current window
#         while window and window[0] == i-K:
#             window.popleft()
#
#         # Remove elements that are less than the current elements
#         while window and A[i] > A[window[-1]]:
#             window.pop()
#
#     # Initialize the deque with the first k elements
#     max_idx = 0
#     for i in range(K):
#         clean_deque(i)
#         window.append(i)
#         if A[i] > A[max_idx]:
#             max_idx = i