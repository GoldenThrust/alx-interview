#!/usr/bin/python3
"""
N-Queens Algorithmn
This script solves the N-Queens problem for a given board size N.
The N-Queens problem involves placing N
queens on an N*N chessboard in such a way that
no two queens threaten each other.

Usage:
    python nqueens.py N

Arguments:
    N (int): The size of the chessboard and the number of queens to be placed.

Example:
>>> ./nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

"""

import sys


def main():
    """
    Main function to solve the N-Queens problem.

    This function reads the board size N from the command-line argument, validates it,
    and initiates the backtracking algorithm to find and print solutions to the N-Queens problem.
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
    Check if placing a queen at a given position is safe.

    Args:
        pos (list): The position [row, col] to check.
        queen_pos (list): List of queen positions.

    Returns:
        bool: True if safe, False otherwise.
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
    Backtrack to find all solutions for placing queens on the board.

    Args:
        row (int): The current row.
        queen_pos (list): List of queen positions.
        num (int): The size of the chessboard.
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
