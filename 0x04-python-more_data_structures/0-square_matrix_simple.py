#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    wordA function that computes the square
    value of all integers of a matrix.
    """"
    copy = matrix.copy()

    for col in range(len(matrix)):
        copy[i] = list(map(lambda x: x**2, matrix[i]))
    return (copy)
