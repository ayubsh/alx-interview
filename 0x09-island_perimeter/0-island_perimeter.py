#!/usr/bin/python3
'''island_perimeter'''


def island_perimeter(grid):
    """
    island_perimeter - calculates the primeter of the island
    @grid: n by n grid
    """
    rows = len(grid)
    cols = len(grid[0])

    result = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                if r == 0 or grid[r-1][c] == 0:
                    result += 1
                if r == rows-1 or grid[r+1][c] == 0:
                    result += 1
                if c == 0 or grid[r][c-1] == 0:
                    result += 1
                if c == cols-1 or grid[r][c+1] == 0:
                    result += 1

    return result
