#!/usr/bin/python3
""" Minumum Operations """


def copy_paste(copied_len, num_oper, num_char):
    """

    """
    num_oper += 2
    copied_len = num_char
    num_char += copied_len

    return [copied_len, num_oper, num_char]


def paste(copied_len, num_oper, num_char):
    """
    
    """
    num_oper += 1
    num_char += copied_len

    return [copied_len, num_oper, num_char]


def minOperations(n):
    """

    """
    if n <= 1:
        return 0

    num_char = 2
    num_oper = 2
    copied_len = 1

    for i in range(n):
        if i <= 1:
            continue

        if n % i == 0 and num_char <= n/2:
            copied_len, num_oper, num_char = copy_paste(
                copied_len, num_oper, num_char)
        elif num_char != n:
            copied_len, num_oper, num_char = paste(
                copied_len, num_oper, num_char)

    return num_oper
