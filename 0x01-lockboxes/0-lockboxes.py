#!/usr/bin/python3

def canUnlockAll(boxes):
    unlocked_boxes = list([0])

    for box in unlocked_boxes:
        for key in boxes[box]:
            if key not in unlocked_boxes and key < len(boxes):
                unlocked_boxes.append(key)

    return len(unlocked_boxes) == len(boxes)
