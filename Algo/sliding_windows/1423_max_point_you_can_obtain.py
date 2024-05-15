# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

"""
1423. Maximum Points You Can Obtain from Cards
Medium
Topics
Companies
Hint
There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.



Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
Example 2:

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.
"""


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # n = len(cardPoints)
        # summ = sum(cardPoints)
        # windowSum = sum(cardPoints[:n - k])
        # ans = summ - windowSum

        # for i in range(k):
        #     windowSum -= cardPoints[i]
        #     windowSum += cardPoints[i + n - k]
        #     ans = max(ans, summ - windowSum)

        # return ans

        total_sum = sum(cardPoints)
        n = len(cardPoints)
        window_sum = sum(cardPoints[:n - k])
        ans = 0

        for i in range(n - k, n):
            ans = max(ans, total_sum - window_sum)
            window_sum += cardPoints[i]
            window_sum -= cardPoints[i - n + k]

        ans = max(ans, total_sum - window_sum)
        return ans