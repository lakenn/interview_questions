# DFS backtracking

"""
def backtrack(state):
    # 1. Base Case: Check if the current state is a solution
    if is_solution(state):
        process_solution(state)  # Do something with the solution (e.g., store or print)
        return

    # 2. Iterate Over Choices: Explore all possible decisions for the current state
    for choice in available_choices(state):
        if is_valid(choice, state):  # Check if the choice is valid under current constraints
            apply_choice(state, choice)  # Make the choice (modify the state)

            # 3. Recur: Move to the next level of the decision tree
            backtrack(state)

            # 4. Undo Choice: Backtrack to the previous state
            undo_choice(state, choice)
"""
from typing import List


def permutation(nums):
    results = []

    def backtracking(path, choices):
        if not choices:
            # do not need path[:] because you are not modifying the path list in-place.
            # Instead, you are creating a new list every time with path + [choices[i]].
            results.append(path)

        for i in range(len(choices)):
            backtracking(path + [choices[i]], choices[:i] + choices[i+1:])

    backtracking([], nums)
    return results


print(permutation([1,2,3]))

def permutation_backtracking(nums):
    results = []
    visited = set()
    current_permutation = [0] * len(nums)
    def backtracking(index):
        if index == len(nums): # reach the end of the tree
            results.append(current_permutation[:])
            return
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                current_permutation[index] = nums[i]
                backtracking(index+1)
                visited.remove(i)

    backtracking(0)
    return(results)

print(permutation_backtracking([1,2,3]))


def subsets(nums):
    result = []

    def backtrack(index, path):
        result.append(path[:])  # Add the current subset
        for i in range(index, len(nums)):
            path.append(nums[i])  # Include nums[i]
            backtrack(i + 1, path)  # Recurse with next index
            path.pop()  # Undo the choice

    backtrack(0, [])
    return result


print(subsets([1,2,3]))

def powerSetPickAlgo(some_list):
    def power_set(index, curr):
        if len(some_list) == index:
            print(curr)
            return

        power_set(index+1, curr + [some_list[index]])
        power_set(index+1, curr)

    power_set(0, [])


def powerSet(some_list):
    results = []
    def power_set(index, curr):
        if len(some_list) == index:
            results.append(curr)
            return

        power_set(index+1, curr + [some_list[index]])
        power_set(index+1, curr)

    power_set(0, [])
    return results


print(powerSet([1,2,3]))


def combinationSum(candidates, target):
    results = []

    def backtracking(index, curr_sum, path):
        # Base case: If the sum equals the target, store the valid combination
        if curr_sum == target:
            results.append(path[:])
            return

        # If the current sum exceeds the target, stop exploring
        if curr_sum > target:
            return

        # Iterate through candidates starting from 'index' to avoid duplicates
        for i in range(index, len(candidates)):
            # Include the candidate in the current path
            path.append(candidates[i])

            # Recur with the same index (because numbers can be reused)
            backtracking(i, curr_sum + candidates[i], path)

            # Backtrack by removing the last added number
            path.pop()

    # Start backtracking with index 0, sum 0, and an empty path
    backtracking(0, 0, [])

    return results


print(combinationSum([2, 3, 6, 7], 7))
# DFS backtracking

# two pointers

# Water Rainfall
def trap(height):
    n = len(height)
    if n == 0:
        return 0
    water = 0
    for i in range(n):
        leftMax = max(height[:i+1])
        rightMax = max(height[i:])
        water += max(0, min(leftMax, rightMax) - height[i])
    return water


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        water = 0

        while left < right:
            if height[left] < height[right]: # it means right and left_max form the container
                water += max(0, left_max - height[left])
                left_max = max(left_max, height[left])
                left += 1
            else:
                water += max(0, right_max - height[right])
                right_max = max(right_max, height[right])
                right -= 1

        return water


def trap(height):
    if not height:
        return 0
    left, right = 0, len(height) - 1
    leftMax, rightMax = 0, 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= leftMax:
                leftMax = height[left]
            else:
                water += leftMax - height[left]
            left += 1
        else:
            if height[right] >= rightMax:
                rightMax = height[right]
            else:
                water += rightMax - height[right]
            right -= 1
    return water

# two pointers