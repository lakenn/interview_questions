def minimum_cost_of_ticket(A):
    result = min_cost_dp(A)
    result = min(result, 25)

    return result


def min_cost_dp(A):
    dp = [0] * len(A)
    dp[0] = 2

    for i in range(1, len(A)):

        # addition of 1-day ticket
        one_day = 2 + dp[i-1]

        # look back
        j = i-1

        # keep moving back until we find the day just
        # right before the day we can buy a 7-day ticket
        while j >= 0 and A[j] >= A[i] - 6:
            j -= 1


        # alternative: 7-day ticket
        seven_day = 7

        # addition of 7-day ticket
        if j > 0:
            seven_day += dp[j]

        dp[i] = min(one_day, seven_day)

    return dp[i]


print(minimum_cost_of_ticket([1,2,4,5,7,29,30]))
print(minimum_cost_of_ticket(range(1, 31)))