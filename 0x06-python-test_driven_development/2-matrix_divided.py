#!/usr/bin/python3
def matrix_divided(matrix, div):
    new_matrix = list(matrix)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be an number")
    elif div is 0:
        raise ZeroDivisionError("division by zero")

    wrong_list = "matrix must be a matrix (list of lists) of integers/floats"
    wrong_size = "Each row of the matrix must have the same size"
    for row in matrix:
        if len(matrix[0]) != len(row):
            raise TypeError(wrong_size)
    for row in matrix:
        for items in row:
            if not isinstance(items, (int, float)):
                raise TypeError(wrong_list)
    new_matrix = []
    for row in matrix:
        new_row = [round(x/div, 2) for x in row]
        new_matrix.append(new_row)
    return (new_matrix)
