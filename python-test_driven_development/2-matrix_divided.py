#!/usr/bin/python3
"""
This module provides a function for dividing all elements of a matrix.
It validates the matrix structure and performs type checking.
All elements are divided by div and rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix: A list of lists of integers or floats
        div: The number to divide by (int or float)

    Returns:
        list: A new matrix with all elements divided by div

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats
        TypeError: If rows are not all the same size
        TypeError: If div is not a number
        ZeroDivisionError: If div is zero
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(error_msg)

    if type(div) is bool or not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_size = None
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(error_msg)
        if len(row) == 0:
            raise TypeError(error_msg)

        if row_size is None:
            row_size = len(row)
        elif len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(error_msg)

    return [[round(element / div, 2) for element in row] for row in matrix]
