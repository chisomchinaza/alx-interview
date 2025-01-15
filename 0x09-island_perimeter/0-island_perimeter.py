#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in the grid.

    Args:
        grid (list of list of int): The grid representing the map.

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    # Directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # If land cell
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # Check if neighbor is water or out of bounds
                    if (nr < 0 or nr >= rows or
                            nc < 0 or nc >= cols or
                            grid[nr][nc] == 0):
                        perimeter += 1

    return perimeter
