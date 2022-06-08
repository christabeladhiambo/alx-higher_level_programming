#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [list(map(lambda x: x * x, elem)) for elem in matrix]
