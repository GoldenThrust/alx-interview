#!/usr/bin/python3
""" 2D Matrix Rotation """


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place.

    Parameters:
    - matrix (List[List[int]]): The 2D matrix to be rotated.

    Example:
    >>> matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
    >>> rotate_2d_matrix(matrix)
    >>> print(matrix)
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]
    """
    for y in range(len(matrix[0])):
        for x in range(y, len(matrix)):
            # Exchange values to perform the rotation
            matrix[y][x], matrix[x][y] = matrix[x][y], matrix[y][x]

    # Reverse each row to complete the rotation
    for y in range(len(matrix)):
        matrix[y].reverse()
