#!/usr/bin/python3
"""Rotate 2d Matrix"""


def rotate_2d_matrix(matrix):
    """Given an n x n 2D matrix
    rotate it 90 degrees clockwise.
    Args:
        matrix (list)
    Does not return anything. The matrix must be edited in-place.
    matrix will have two dimensions and is not empty
    """
    # print original matrix
    for row in matrix:
        print(row)
    row = []
    column = []
    # 90 degree rotation can be achieved using swapping inplace
    # conditions:
    #   swap when index is only different digits eg.01, 21
    #   then finally reverse the rows
    if len(matrix) == 2:
        print("doesnt apply for now")
    index = len(matrix)
    for row in range(0, len(matrix) - 1):
        for col in range(0, len(matrix) - 1):
            if row < col:
                tmp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = tmp
    # finaly reverse the rows
    for row in matrix:
        row = row.reverse()


