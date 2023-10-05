#!/usr/bin/python3
"""given n number of locked boxes it retuns weather it can be
unlocked
"""


def canUnlockAll(boxes):
    unlocked = set([0])
    keys = set()

    for i, box in enumerate(boxes):
        keys.update(box)
        if i in unlocked:
            unlocked.update(box)

    return len(unlocked) == len(boxes)
