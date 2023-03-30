#!/usr/bin/python3
"""Lockbox Challange"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened or not
        Returns:
        True: all boxes can be opened
        False: not all boxes can be opened
    """
    n = len(boxes)
    checked = set([0])
    unchecked = set(boxes[0]).difference(set([0]))

    while len(unchecked) > 0:
        box = unchecked.pop()
        if not box or box >= n or box < 0:
            continue
        if box not in checked:
            unchecked = unchecked.union(boxes[box])
            checked.add(box)
    return n == len(checked)
    