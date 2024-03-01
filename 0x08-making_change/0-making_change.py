#!/usr/bin/python3
""" Making Changes """


def makeChange(coins, total):
    """
    A dynamic programming solution to find the minimum number of coins
    needed to make change for a given total.

    Usage:
        result = makeChange(coins, total)

    Parameters:
        coins (List[int]): A list of coin denominations available.
        total (int): The total amount for which we want to make change.

    Returns:
        int: The minimum number of coins needed to make change for the
        given total. If it's not possible to make exact change, returns -1.
    """
    if total <= 0:
        return 0

    best_answers = [float('inf')] * (total + 1)
    best_answers[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            best_answers[amount] = min(best_answers[amount],
                                       best_answers[amount - coin] + 1)

    return best_answers[total] if best_answers[total] != float('inf') else -1
