#!/usr/bin/python3
"""given n number of locked boxes it retuns weather it can be
unlocked
"""


def canUnlockAll(boxes):
    n = len(boxes)
    sboxes = set([0])
    uboxes = set(boxes[0]).difference(set([0]))

    while len(uboxes) > 0:
        boxIdx = uboxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in sboxes:
            uboxes = uboxes.union(boxes[boxIdx])
            sboxes.add(boxIdx)
    return len(sboxes) == n
