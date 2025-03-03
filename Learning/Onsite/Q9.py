"""
max profit with 1 buy and 1 sell
"""

def sol(prices):
    # kadane algo
    # max_profit, curr_profit
    buy = prices[0]
    for idx in range(1, len(prices)):
        curr_profit = prices[idx] - buy
        max_profit = max(max_profit, curr_profit)
        # encounter a lower buy
        if prices[idx] < buy:
            buy = prices[idx]

    return max_profit

def sol_brute_force(prices):
    max_profit = 0

    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            max_profit = max(max_profit, prices[j] - prices[i])

    return max_profit