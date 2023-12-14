#!/usr/bin/python3
"""Module for matrix_divided method"""


def matrix_divided(matrix, div):
    """Divides all elements of matrix by div
    Args:
        matrix: list of lists containing int or float
        div: number to divid a matrix by
    Returns:
        list: list of lists representing divided matrix
    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        TypeError: division by zero
        ZeroDivisionError: if div is zero
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)" +
                        "of int/float")
    for row in matrix:
        if not isintance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of in/float")
    if len(row) != len(matrix[0]):
        raise TypeError("Each row of the matrix must have the same size")
    for x in row:
        if not isinstance(x, (int, float)):
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of int /float")
    return [[round(x / div, 2) for x in row] for row in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
