#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_squared = []
    for i in matrix:
        matrix_squared.append([j**2 for j in i])
    return matrix_squared
