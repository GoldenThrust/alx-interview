#!/usr/bin/python3
import sys
from time import sleep

try:
    num = sys.argv[1]
except IndexError:
    print("Usage: nqueens N")
    sys.exit(1)

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)


try:
    num = int(num)
except ValueError:
    print("N must be a number")
    sys.exit(1)

if num < 4:
    print("N must be at least 4")
    sys.exit(1)


def is_safe(pos, queen_pos):
    for j in reversed(range(pos[0])):
        if (
            [j, pos[1]] in queen_pos
            or [j, pos[1] - (pos[0] - j)] in queen_pos
            or [j, pos[1] + (pos[0] - j)] in queen_pos
        ):
            return False
    return True


def backtrack(row, queen_pos, depth):
    if row == num:
        board = [[0] * num for _ in range(num)]

        sleep(1)
        print(f"New Solution")
        for pos in queen_pos:
            sleep(1)
            board[pos[0]][pos[1]] = 1
            for board_row in board:
                print(board_row, flush=True)
            print()
        return

    for col in range(num):
        if is_safe([row, col], queen_pos):
            queen_pos.append([row, col])
            backtrack(row + 1, queen_pos, depth + 1)
            queen_pos.pop()


for i in range(num):
    queen_pos = [[0, i]]
    backtrack(1, queen_pos, 0)
