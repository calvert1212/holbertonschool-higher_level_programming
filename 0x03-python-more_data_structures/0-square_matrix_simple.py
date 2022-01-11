#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    xmatrix = [[element**2 for element in row] for row in matrix]
    return xmatrix
