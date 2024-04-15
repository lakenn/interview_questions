from collections import deque
from typing import List

def sliding_window_maximum(nums: List[int], k: int) -> List[int]:
    q = deque()
    res = []
    for i, cur in enumerate(nums):
        while q and nums[q[-1]] <= cur:
            q.pop()

        q.append(curr)