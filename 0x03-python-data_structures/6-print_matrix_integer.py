#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print('{:d}'.format(" ".join(map(str, row))))
