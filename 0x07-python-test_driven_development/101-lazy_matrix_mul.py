#!/usr/bin/python3
"""
A module that prints two matrices using Numpy module
"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    try:
        result = np.matmul(m_a, m_b)
        return result
    except ValueError:
        raise ValueError("Input matrices are not compatible for multiplication")
    except Exception as e:
        raise Exception("An error occurred during matrix multiplication: {}".format(str(e)))

