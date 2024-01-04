#!/usr/bin/python3
""" Pascal Triangle """


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to a specified number of rows.

    Args:
    - n (int): The number of rows for the Pascal's triangle.

    Returns:
    - list: A list of lists representing Pascal's triangle up to `n` rows.
      Each inner list represents a row in the triangle.

    Examples:
    >>> pascal_triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

    >>> pascal_triangle(0)
    []
    """
    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        row = [None] * (i + 1)
        row[0] = 1

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        if i > 0:
            row[i] = 1

        triangle.append(row)

    return triangle
