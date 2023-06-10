#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    row_index = 0
    while row_index < len(matrix):
        row = matrix[row_index]
        elem_index = 0
        while elem_index < len(row):
            print('{:d}'.format(row[elem_index]), end=(" " if elem_index < len(row) - 1 else ""))
            elem_index += 1
        row_index += 1

