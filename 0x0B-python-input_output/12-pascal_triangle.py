#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Generate Pascal's Triangle of size n.

    Args:
        n (int): The size of the Pascal's Triangle to generate.

    Returns:
        list: A list of lists of integers representing Pascal's Triangle.
              Each sublist represents a row in the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for _ in range(n - 1):
        row = [1]
        for j in range(1, len(triangle[-1])):
            row.append(triangle[-1][j - 1] + triangle[-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
