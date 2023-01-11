#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    # use map() and list comprehension
    return [list(map(lambda x: x**2, row)) for row in matrix]
