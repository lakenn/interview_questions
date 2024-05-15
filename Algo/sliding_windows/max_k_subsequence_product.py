from typing import List
import numpy

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        product_sum = 1
        for num in cardPoints:
            product_sum *= num

        cardPoints.sort()




        n = len(cardPoints)
        window_sum = numpy.product(cardPoints[:n - k])
        ans = 0

        for i in range(n - k, n):
            ans = max(ans, product_sum / window_sum)
            window_sum *= cardPoints[i]
            window_sum /= cardPoints[i - n + k]

        ans = max(ans, product_sum/window_sum)
        return ans

# print(Solution().maxScore([1, 2, -1, -3, -6, 4], 4))


def maxProductSubsequence(arr, k):
    arr.sort()
    n = len(arr)
    maxProduct = 1

    if k <= n // 2:
        # Consider the product of the k largest elements
        for i in range(n - 1, n - k - 1, -1):
            maxProduct *= arr[i]
    else:
        # Consider the product of the k smallest and the largest elements
        left = 0
        right = n - 1

        # Include the smallest k elements
        while k > 1:
            if arr[left] * arr[left + 1] > arr[right] * arr[right - 1]:
                maxProduct *= arr[left] * arr[left + 1]
                left += 2
            else:
                maxProduct *= arr[left]
                left += 1
            k -= 2

        # Include the largest remaining element
        if k == 1:
            maxProduct *= arr[right]

    return maxProduct


# Example usage:
arr = [1, 2, -3, 4, 5]
k = 3
print(maxProductSubsequence(arr, k))  # Output: 20
