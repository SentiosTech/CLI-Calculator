# test_calculator.py

"""
Unit tests for the calculator module functions.
These tests verify the correctness of arithmetic operations such as:
square root, power, addition, subtraction, multiplication, and division.
"""

from calculator.calculator import square_root, power, sume, subtract, multiply, division

def test_square_root():
    """
    Tests the square_root function with basic inputs.
    """
    assert square_root(9) == 3
    assert square_root(0) == 0

def test_power():
    """
    Tests the power function with positive and zero exponents.
    """
    assert power(2, 3) == 8
    assert power(5, 0) == 1

def test_sume():
    """
    Tests the sume (addition) function with positive numbers.
    """
    assert sume(4, 5) == 9
    assert sume(-1, 1) == 0

def test_subtract():
    """
    Tests the subtract function with positive integers.
    """
    assert subtract(7, 3) == 4
    assert subtract(5, 10) == -5

def test_multiply():
    """
    Tests the multiply function with positive integers.
    """
    assert multiply(4, 2) == 8
    assert multiply(0, 10) == 0

def test_division():
    """
    Tests the division function with valid inputs (non-zero denominator).
    """
    assert division(8, 2) == 4
    assert division(10, 5) == 2
