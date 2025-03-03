"""

The Collatz Conjecture says if you take a positive integer N and
repeatedly set either N=N/2 (if it's even) or N=3N+1 (if it's odd), N will eventually be 1.
5 -> 16 -> 8 -> 4 -> 2 -> 1 (5 steps).


Given N, how many steps does it take to reach 1?

"""
# https://leetcode.com/problems/sort-integers-by-the-power-value/description/
from collections import deque

"""
            Start
         /         \
    Start/2         3*Start+1

"""

"""
Default Argument Behavior: The default argument (memo={}) is initialized only once, 
when the function is first defined. 
If the function is called multiple times, the dictionary will retain its contents between calls. 
If you want to reset the cache for each function call, you could modify the function to not use the default mutable argument like this:
def transformNum2(n, memo=None):
    if memo is None:
        memo = {}
    ...
This ensures that memo is reinitialized as an empty dictionary each time the function is called without carrying over cached results from previous calls.
"""
def transformNum2(n, memo={}):
    # Base case: if n is 1, we are done
    if n == 1:
        return 0

    # If the result for n is already cached, return it
    if n in memo:
        return memo[n]

    # If n is even, recursively call with n // 2
    if n % 2 == 0:
        result = 1 + transformNum2(n // 2, memo)
    # If n is odd, recursively call with 3*n + 1
    else:
        result = 1 + transformNum2(3 * n + 1, memo)

    # Cache the result for the current n
    memo[n] = result
    return result


# Test the function
print(transformNum2(6))  # Example: It will output the number of steps to reach 1


def sol2(start):
    step = 0

    while start != 1:
        step += 1
        if start & 1 == 0:
            start //= 2
        else:
            start = 3*start + 1

    return step
# stupid as There is no choice or multiple possibilities for how to proceed from any given state.
def sol(start):
    if start == 0:
        return -1

    step = 0
    queue = deque([(start, step)])
    visited = set()

    while queue:
        num, step = queue.popleft()

        if num == 1:
            return step

        if num % 2 == 0 and num/2 not in visited:
            visited.add(num/2)
            queue.append((num/2, step+1))
        elif 3*num + 1 not in visited:
            visited.add(3*num+1)
            queue.append((3*num+1, step+1))

    return step

print(sol2(5))