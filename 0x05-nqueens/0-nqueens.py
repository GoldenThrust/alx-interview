#!/usr/bin/python3
"""
N-Queens
"""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    num = int(sys.argv[1])
except Exception:
    print("N must be a number")
    sys.exit(1)

if num < 4:
    print("N must be at least 4")
    sys.exit(1)


def is_safe(pos, queen_pos):
    """
    Check if placing a queen at a given position is safe.

    Args:
        pos (list): The position [row, col] to check.
        queen_pos (list): List of queen positions.

    Returns:
        bool: True if safe, False otherwise.
    """
    for j in reversed(range(pos[0])):
        if (
            [j, pos[1]] in queen_pos
            or [j, pos[1] - (pos[0] - j)] in queen_pos
            or [j, pos[1] + (pos[0] - j)] in queen_pos
        ):
            return False
    return True


def backtrack(row, queen_pos):
    """
    Backtrack to find all solutions for placing queens on the board.

    Args:
        row (int): The current row.
        queen_pos (list): List of queen positions.
    """
    if row == num:
        print(queen_pos)
        return

    for col in range(num):
        if is_safe([row, col], queen_pos):
            queen_pos.append([row, col])
            backtrack(row + 1, queen_pos)
            queen_pos.pop()


if __name__ == "__main__":
    for i in range(num):
        queen_pos = [[0, i]]
        backtrack(1, queen_pos)
