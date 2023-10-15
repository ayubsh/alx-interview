#!/usr/bin/env python3
"""Minimum opreation """


def minOperations(n: int) -> int:
    """minimun ops
    """
    if not isinstance(n, int):
        return 0

    ops_count = 0
    clipboard = 0
    done = 1

    while done < n:
        if clipboard == 0:
            # Initialize - copy all and first paste
            clipboard = done
            done += clipboard
            ops_count += 2
        elif n - done > 0 and (n - done) % done == 0:
            # Copy all and paste to double characters
            clipboard = done
            done += clipboard
            ops_count += 2

        else:
            # Paste to incrementally add characters
            done += clipboard
            ops_count += 1
    return ops_count
