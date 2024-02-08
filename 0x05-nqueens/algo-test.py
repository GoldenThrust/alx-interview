import sys

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


def recurse(row, queen_pos, depth):
    print(row, queen_pos, depth)
    if row == num:
        print(queen_pos)
        return

    for col in range(num):
        if is_safe([row, col], queen_pos):
            queen_pos.append([row, col])
            recurse(row + 1, queen_pos, depth + 1)
            queen_pos.pop()


for i in range(num):
    queen_pos = [[0, i]]
    recurse(1, queen_pos, 0)
