from typing import List
import numpy

# class Solution:
#     def maxScore(self, cardPoints: List[int], k: int) -> int:
#         product_sum = 1
#         for num in cardPoints:
#             product_sum *= num
#
#         cardPoints.sort()
#         n = len(cardPoints)
#         window_sum = numpy.product(cardPoints[:n - k])
#         ans = 0
#
#         for i in range(n - k, n):
#             ans = max(ans, product_sum / window_sum)
#             window_sum *= cardPoints[i]
#             window_sum /= cardPoints[i - n + k]
#
#         ans = max(ans, product_sum/window_sum)
#         return ans

# print(Solution().maxScore([1, 2, -1, -3, -6, 4], 4))


def maxProductSubsequence(arr, k):
    if k == 0:
        return 0

    arr.sort()
    n = len(arr)
    maxProduct = 1

    left, right = 0, n-1

    if k % 2 == 1:
        maxProduct *= arr[right]
        right -= 1
        k -= 1

    if maxProduct < 0:
        while k > 0:
            maxProduct *= arr[right]
            k -= 1
        return maxProduct

    while k >= 2:
        if arr[left] * arr[left+1] > arr[right]*arr[right-1]:
            maxProduct *= arr[left] * arr[left+1]
            left += 2
        else:
            maxProduct *= arr[right]*arr[right-1]
            right -= 2
        k -= 2

    return maxProduct


# Example usage:
arr = [1, 2, -1, -3, -6, 4]
k = 4
arr = [-1, -10, 9, -3, 5, -8, 1, -5, -6, -3, -9, -10, 2, -2, 2, 7, -6, 2, 10, -8]
k = 5
arr = [10, -8, 6, 7, 1, 1, 8, -3, -3, 5, -4, 6, 7]
k = 8
arr = [-1, -9, -13, -9]
k = 3
print(maxProductSubsequence(arr, k))  # Output: 20
