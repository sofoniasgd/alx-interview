#!/usr/bin/python3
"""0. Island Perimeter"""


def island_perimeter(grid):
    """ A function that returns the perimeter of the island described in grid
        grid is a list of list of integers
            0 represents water
            1 represents land
            Each cell is square, with a side length of 1
        Cells are connected horizontally/vertically (not diagonally).
        grid is rectangular, with its width and height not exceeding 100
        Args:
            grid (list)
        Return:
            perimeter of the island
    """
    # algorithm:
    # terate over every list element(cell)
    # for every land, check all surrounding cells
    # for every adjecent corner if surrounding cells dont exist,
    # add 1 to perimeter value
    perimeter = 0
    neighbours = [None] * 4
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            # get neighbor cells left, right, top, buttom
            neighbours[0] = grid[row][col - 1] if col - 1 >= 0 else 0
            neighbours[1] = grid[row][col + 1] if col + 1 < len(grid[0]) else 0
            neighbours[2] = grid[row - 1][col] if row - 1 >= 0 else 0
            neighbours[3] = grid[row + 1][col] if row + 1 < len(grid) else 0
            # now add the perimeter
            for neighbour in neighbours:
                if grid[row][col] == 1 and neighbour == 0:
                    perimeter += 1
    return perimeter
