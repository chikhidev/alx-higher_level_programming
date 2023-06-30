#!/usr/bin/python3
"""
This is the matrix_mul module.

This module supplies one function, matrix_mul().
"""


def matrix_mul(m_a, m_b):
    """
    Return a new matrix multiplied.

    Args:
        m_a (list): list of lists of integers or floats.
        m_b (list): list of lists of integers or floats.

    Raises:
        TypeError: If m_a or m_b is not a list, or if any row in m_a or m_b is not a list.
        ValueError: If m_a or m_b is empty, if any row in m_a or m_b is empty,
                    if the rows in m_a and m_b are not of compatible sizes,
                    or if m_a and m_b cannot be multiplied.

    Returns:
        list: The multiplied matrix.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for row_a in m_a:
        if not isinstance(row_a, list):
            raise TypeError("m_a must be a list of lists")
    for row_b in m_b:
        if not isinstance(row_b, list):
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    for row_a in m_a:
        if len(row_a) == 0:
            raise ValueError("m_a can't contain empty rows")

    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    for row_b in m_b:
        if len(row_b) == 0:
            raise ValueError("m_b can't contain empty rows")

    for row_a in m_a:
        for i in row_a:
            if not isinstance(i, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row_b in m_b:
        for i in row_b:
            if not isinstance(i, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    row_a_len = len(m_a[0])
    for row_a in m_a:
        if len(row_a) != row_a_len:
            raise TypeError("each row of m_a must be of the same size")
    row_b_len = len(m_b[0])
    for row_b in m_b:
        if len(row_b) != row_b_len:
            raise TypeError("each row of m_b must be of the same size")

    if row_a_len != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return [[sum(a * b for a, b in zip(row_a, col_b))
             for col_b in zip(*m_b)] for row_a in m_a]

