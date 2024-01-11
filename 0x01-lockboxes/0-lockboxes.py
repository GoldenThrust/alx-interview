#!/usr/bin/python3
""" Can unlocked All """


def canUnlockAll(boxes):
    """
    Determines whether it is possible to unlock all boxes in a given list.

    Args:
    - boxes (list of lists): A list where each index represents a box, and the value at that index is a list of keys.

    Returns:
    - bool: True if all boxes can be unlocked, False otherwise.

    Examples:
    >>> canUnlockAll([[1], [2], [3], [4], []])
    True
    >>> canUnlockAll([[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]])
    False
    """

    unlocked_boxes = [0]

    for box in unlocked_boxes:
        for key in boxes[box]:
            if key not in unlocked_boxes and key < len(boxes):
                unlocked_boxes.append(key)

    return len(unlocked_boxes) == len(boxes)
