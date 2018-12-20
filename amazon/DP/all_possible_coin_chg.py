def all_possible_coin_chg_recur(V, coins, m):
    if V == 0:
        return 1

    if m == 0 and V > 0:
        return 0

    if V < 0:
        return 0

    return all_possible_coin_chg_recur(V-coins[m-1], coins, m) + all_possible_coin_chg_recur(V, coins, m-1)


def all_possible_coin_chg(V, coins, m):
    dp = [[0 for col in range(V+1)] for row in range(m)]

    # base case, V == 0
    for i in range(m):
        dp[i][0] = 1

    for i in range(m):
        for j in range(1, V+1):
            y = dp[i-1][j] if i > 0 else 0

            x = dp[i][j - coins[i]] if j - coins[i] >= 0 else 0

            dp[i][j] = x + y

    return dp[m-1][V]

coins = [1,2]
print(all_possible_coin_chg_recur(3, coins, len(coins)))
print(all_possible_coin_chg(3, coins, len(coins)))