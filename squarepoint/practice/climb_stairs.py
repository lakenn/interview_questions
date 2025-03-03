# ways(i)=ways(i−1)+ways(i−2)

def climbStairs(n):
    if n <= 1:
        return 1

    # DP array to store the number of ways to reach each step
    dp = [0] * (n + 1)

    # Base cases
    dp[0] = 1  # One way to stay at the ground (0th step)
    dp[1] = 1  # One way to reach the first step

    # Fill the DP table
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    # The result is the number of ways to reach the nth step
    return dp[n]


# Example usage
n = 5
print(climbStairs(n))  # Output: 8


def climbStairs(n):
    if n <= 1:
        return 1

    # Initialize the two variables for the last two steps
    prev2, prev1 = 1, 1

    # Compute the number of ways to reach each step from 2 to n
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1


# Example usage
n = 5
print(climbStairs(n))  # Output: 8
