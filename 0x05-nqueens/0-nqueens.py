#!/usr/bin/python3
"""
N-Queens Algorithmn
"""

import sys


def main():
    """
    Main function to solve the N-Queens
    """

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        num = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        exit(1)

    if num < 4:
        print("N must be at least 4")
        exit(1)

    for i in range(num):
        queen_pos = [[0, i]]
        backtrack(1, queen_pos, num)


def is_safe(pos, queen_pos):
    """
    Check safe placing of queen
    """

    for j in reversed(range(pos[0] + 1)):
        if (
            [j, pos[1]] in queen_pos
            or [j, pos[1] - (pos[0] - j)] in queen_pos
            or [j, pos[1] + (pos[0] - j)] in queen_pos
        ):
            return False
    return True


def backtrack(row, queen_pos, num):
    """
    Backtrack to find all solutions
    """

    if row == num:
        print(queen_pos)
        return

    for col in range(num):
        if is_safe([row, col], queen_pos):
            queen_pos.append([row, col])
            backtrack(row + 1, queen_pos, num)
            queen_pos.pop()


if __name__ == "__main__":
    main()
