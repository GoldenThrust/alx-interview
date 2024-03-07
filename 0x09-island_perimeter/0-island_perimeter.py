#!/usr/bin/python3
""" Island Perimeter """


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the given grid.

    Args:
    - grid (List[List[int]]): A rectangular grid representing
    an island, where 0 represents water and 1 represents land.

    Returns:
    - int: The perimeter of the island.


    The perimeter is calculated by assuming each
    land cell contributes 4 to
    the perimeter, and then adjusting for shared
    borders with neighboring
    land cells.
    """
    perimeter = 0

    if not grid or not grid[0]:
        return perimeter

    x, y = len(grid), len(grid[0])

    for i in range(x):
        for j in range(y):
            if grid[i][j] == 1:
                perimeter += 4

                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

    return perimeter
