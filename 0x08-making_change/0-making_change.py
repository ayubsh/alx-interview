#!/usr/bin/python3
'''Making change'''


def makeChange(coins, total):
    """
    takes coins and total and
    returns the number of coins needed to makeChange
    """
    if total <= 0:
        return 0

    def helper(total, coins, memo):
        if total < 0:
            return float('inf')
        if total == 0:
            return 0
        if total in memo:
            return memo[total]
        res = float('inf')
        for coin in coins:
            res = min(res, helper(total - coin, coins, memo) + 1)
        memo[total] = res
        return res
    memo = {}
    res = helper(total, coins, memo)
    return res if res != float('inf') else -1
