# https://workat.tech/problem-solving/practice/distinct-numbers-window
from collections import defaultdict
from typing import List

'''
Given an array A and a value k, find the number of distinct elements in each window (subarray) of size k.

Example
A: [1, 1, 2, 1, 4, 6, 5]
k: 3
Result: [2, 2, 3, 3, 3]
'''
class Solution:
    def distinctNumbersInWindow(self, A: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)  # Dictionary to store the frequency of numbers

        left = right = 0
        ans = []

        while right in range(len(A)):
            frequency[A[right]] += 1

            if right - left + 1 == k:
                ans.append(len(frequency))
                frequency[A[left]] -= 1
                if frequency[A[left]] == 0:
                    del frequency[A[left]]
                # we need to start moving left ptr once we reach window size k
                left += 1

        return ans


print(Solution().distinctNumbersInWindow([1,1,2,1,4,6,5], 3))
