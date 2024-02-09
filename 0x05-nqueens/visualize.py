import sys
import pygame
from pygame.locals import QUIT
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

pygame.init()

solution = 1
cell_size = 50
width, height = num * cell_size, num * cell_size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("N-Queens Visualization")

def is_safe(pos, queen_pos):
    for j in reversed(range(pos[0])):
        if (
            [j, pos[1]] in queen_pos
            or [j, pos[1] - (pos[0] - j)] in queen_pos
            or [j, pos[1] + (pos[0] - j)] in queen_pos
        ):
            return False
    return True

def draw_board(queen_pos):
    screen.fill((255, 255, 255))

    for i in range(num + 1):
        pygame.draw.line(screen, (0, 0, 0), (0, i * cell_size), (width, i * cell_size))
        pygame.draw.line(screen, (0, 0, 0), (i * cell_size, 0), (i * cell_size, height))

    for pos in queen_pos:
        pygame.draw.circle(screen, (0, 0, 0), (pos[1] * cell_size + cell_size // 2, pos[0] * cell_size + cell_size // 2), cell_size // 4)

    pygame.display.flip()


def backtrack(row, queen_pos):
    global solution
    if row == num:
        print(f"Solution {solution}")
        solution += 1
        draw_board(queen_pos)
        sleep(0.2 * num)
        return

    for col in range(num):
        if is_safe([row, col], queen_pos):
            queen_pos.append([row, col])
            draw_board(queen_pos)
            sleep(0.001 * num)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            backtrack(row + 1, queen_pos)
            queen_pos.pop()
            draw_board(queen_pos)
            sleep(0.001 * num)


for i in range(num):
    queen_pos = [[0, i]]
    backtrack(1, queen_pos)

pygame.quit()
