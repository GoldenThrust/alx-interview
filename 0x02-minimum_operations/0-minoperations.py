#!/usr/bin/python3
""" Minumum Operations """


def minOperations(n):
    """
    Calculate the minimum number of operations to reach the target number.

    Parameters:
    - n (int): Target number.

    Returns:
    - int: Minimum number of operations.
    """

    if n <= 1:
        return 0

    num_oper = 0
    copied_len = 0
    num_char = 1

    while num_char < n:
        if n % num_char == 0:  # copy and paste
            copied_len = num_char
            num_char += copied_len
            num_oper += 2
        else:  # paste only
            num_char += copied_len
            num_oper += 1

    return num_oper
