#!/usr/bin/python3

""""function that divides all elements of a matrix"""

def matrix_divided(matrix, div):
    """
    matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception with the message matrix must be a matrix (list of lists) of integers/floats
Each row of the matrix must be of the same size, otherwise raise a TypeError exception with the message Each row of the matrix must have the same size
div must be a number (integer or float), otherwise raise a TypeError exception with the message div must be a number
div can’t be equal to 0, otherwise raise a ZeroDivisionError exception with the message division by zero
All elements of the matrix should be divided by div, rounded to 2 decimal places
Returns a new matrix
    """
    # Check if matrix is a list of non-empty lists containing only integers or floats
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be matrix of ints/floats")

    # Check if all rows have the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of matrix must have same size")

    # Check if div is an integer or a float
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be num")

    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Create a new matrix containing the results of the division
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    # Return the new matrix
    return new_matrix
