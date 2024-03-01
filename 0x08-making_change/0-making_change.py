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

    arr_changes = [float('inf')] * (total + 1)
    arr_changes[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            arr_changes[amount] = min(arr_changes[amount],
                                       arr_changes[amount - coin] + 1)

    # return arr_changes[total] if arr_changes[total] != float('inf') else -1
    if arr_changes[total] != float('inf'):
        return arr_changes[total]
    else:
        return -1
