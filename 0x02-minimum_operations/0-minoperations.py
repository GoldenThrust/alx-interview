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

    num_char = 2
    num_oper = 2
    copied_len = 1

    for i in range(2, n):
        if n % i == 0 and num_char <= n // 2:
            copied_len, num_oper, num_char = copy_paste(
                copied_len, num_oper, num_char)
        else:
            copied_len, num_oper, num_char = paste(
                copied_len, num_oper, num_char)

        if num_char >= n:
            break

    return num_oper


def copy_paste(copied_len, num_oper, num_char):
    """
    Copy and paste operation.

    Parameters:
    - copied_len (int): Length of the copied text.
    - num_oper (int): Current number of operations.
    - num_char (int): Current number of characters.

    Returns:
    - List[int]: Updated values for copied_len, num_oper, and num_char.
    """
    num_oper += 2
    copied_len = num_char
    num_char += copied_len

    return [copied_len, num_oper, num_char]


def paste(copied_len, num_oper, num_char):
    """
    Paste operation.

    Parameters:
    - copied_len (int): Length of the copied text.
    - num_oper (int): Current number of operations.
    - num_char (int): Current number of characters.

    Returns:
    - List[int]: Updated values for copied_len, num_oper, and num_char.
    """
    num_oper += 1
    num_char += copied_len

    return [copied_len, num_oper, num_char]
