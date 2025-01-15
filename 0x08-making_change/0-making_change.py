#!/usr/bin/python3
"""
Module to solve the coin change problem using dynamic programming.
"""


def makeChange(coins, total):
    """
    Determine the minimum number of coins required to meet a given total.

    Args:
        coins (list): List of the values of coins available.
        total (int): The total amount to make.

    Returns:
        int: Minimum number of coins needed or -1 if total cannot be met.
    """
    if total <= 0:
        return 0

    # Initialize dp array with infinity
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Build dp array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means total cannot be made
    return dp[total] if dp[total] != float('inf') else -1
