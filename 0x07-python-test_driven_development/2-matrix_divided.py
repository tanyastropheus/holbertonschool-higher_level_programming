#!/usr/bin/python3
def matrix_divided(matrix, div):
    """a function that divides all elements of a matrix

    Args:
        matrix (list): list of lists of integers/floats.
        div (int/float): a non-zero number that matrix is divided by

    Returns:
        A new matrix.
        All elements of the new matrix are rounded to 2 decimal places

    Raises:
        TypeError: when div or elements of lists in matrix is not int/float,
                   or when rows in the matrix are of different sizes
        ZeroDivisionError: when div is zero

    """
    type_err = "matrix must be a matrix (list of lists) of integers/floats"

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if len(matrix) == 0:
        raise TypeError(type_err)

    for row in matrix:
        if type(row) is not list:
            raise TypeError(type_err)

        for i in row:
            if type(i) not in [int, float]:
                raise TypeError(type_err)

        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for row in matrix:
        new_matrix.append([round((elem / div), 2) for elem in row])
    return new_matrix
