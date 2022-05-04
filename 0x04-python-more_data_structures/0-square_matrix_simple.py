#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        return [[j * j for j in a] for a in matrix]
