#!/usr/bin/python3

"""
Multiplies 2 matrices by using 'numpy' module.
"""
import numpy as lazy


def lazy_matrix_mul(m_a, m_b):
    """
    Function to multiplies 2 matrices.
    m_a: As a list of lists.
    m_b: As a list of lists.
    Return: The resulting matrix.
    """
    return lazy.matmul(m_a, m_b)
