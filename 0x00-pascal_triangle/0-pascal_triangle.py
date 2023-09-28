#!/usr/bin/python3
"""
0-pascal_triangle - print
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    pascal = [[1]]

    for i in range(1, n):
        """
            creates the pascal triangle
        """
        row = [1]
        ls_row = pascal[-1]
        row += [ls_row[j], ls_row[j+1] for j in range(len(ls_row) - 1)]
        row.append(1)
        pascal.append(row)

    return pascal
