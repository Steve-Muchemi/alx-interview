#!/usr/bin/python3
"""
This module contains a function that solves the lockboxes problem
"""


def canUnlockAll(boxes):
    """
    Takes in the keys of each box then uses them to unlock boxes/
    that with a matching index.

    Args:
    boxes : a list of lists
    Returns:
    bool: True if all boxes can be unlocked, false if otherwise
    """
    lockbox_count = len(boxes)

    if lockbox_count:
        keys = boxes[0]
        boxes[0] = [-1]
        while keys:
            new_keys = []
            for key in keys:
                if key < lockbox_count:
                    if boxes[key] != [-1]:
                        new_keys += boxes[key]
                        boxes[key] = [-1]
            keys = new_keys
        if boxes.count([-1]) == lockbox_count:
            return True
        else:
            return False
