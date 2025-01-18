import pytest
import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from coaching_dev.fibo_matrix import FiboMatrix

def test_fibo_matrix_square():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = [[1, 1, 2], [3, 5, 8], [13, 21, 34]]
    fibo_matrix = FiboMatrix(matrix)
    result = fibo_matrix.solve_matrix()
    assert np.array_equal(result, np.array(expected))

def test_fibo_matrix_rectangular():
    matrix = [[1, 2], [3, 4], [5, 6]]
    expected = [[1, 1], [2, 3], [5, 8]]
    fibo_matrix = FiboMatrix(matrix)
    result = fibo_matrix.solve_matrix()
    assert np.array_equal(result, np.array(expected))

def test_fibo_matrix_empty():
    matrix = []
    expected = []
    fibo_matrix = FiboMatrix(matrix)
    result = fibo_matrix.solve_matrix()
    assert np.array_equal(result, np.array(expected))

def test_fibo_matrix_single_element():
    matrix = [[5]]
    expected = [[5]]
    fibo_matrix = FiboMatrix(matrix)
    result = fibo_matrix.solve_matrix()
    assert np.array_equal(result, np.array(expected))

def test_fibo_matrix_large_numbers():
    matrix = [[10, 15], [20, 25]]
    expected = [
        [55, 610],
        [6765, 75025],
    ]
    fibo_matrix = FiboMatrix(matrix)
    result = fibo_matrix.solve_matrix()
    assert np.array_equal(result, np.array(expected))

def test_fibo_matrix_negative_and_zero():
    matrix = [[-1, 0], [1, 2]]
    expected = [[0, 0], [1, 1]]
    fibo_matrix = FiboMatrix(matrix)
    result = fibo_matrix.solve_matrix()
    assert np.array_equal(result, np.array(expected))

if __name__ == "__main__":
    pytest.main()
