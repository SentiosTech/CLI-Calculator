# calculator.py

"""
This module provides basic arithmetic functions and an input handler for a simple calculator.
Supported operations include square root, power, addition, subtraction, multiplication, and division.
"""

import math

def square_root(num1):
    """
    Returns the square root of the given number.

    Parameters:
        num1 (float): A non-negative number.

    Returns:
        float: The square root of num1.
    """
    return math.sqrt(num1)

def power(base, exponent):
    """
    Raises the base to the power of the exponent.

    Parameters:
        base (float): The base number.
        exponent (float): The exponent.

    Returns:
        float: The result of base ** exponent.
    """
    return base ** exponent

def sume(num1, num2):
    """
    Returns the sum of two numbers.

    Parameters:
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The sum of num1 and num2.
    """
    return num1 + num2

def subtract(num1, num2):
    """
    Returns the result of subtracting num2 from num1.

    Parameters:
        num1 (float): The number to subtract from.
        num2 (float): The number to subtract.

    Returns:
        float: The result of num1 - num2.
    """
    return num1 - num2

def multiply(num1, num2):
    """
    Returns the product of two numbers.

    Parameters:
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The product of num1 and num2.
    """
    return num1 * num2

def division(num1, num2):
    """
    Returns the result of dividing num1 by num2.

    Parameters:
        num1 (float): The numerator.
        num2 (float): The denominator (must not be zero).

    Returns:
        float: The result of num1 / num2.

    Raises:
        ZeroDivisionError: If num2 is zero.
    """
    return num1 / num2

def get_float_input(prompt):
    """
    Continuously prompts the user for a number until a valid float is entered.

    Parameters:
        prompt (str): The message shown to the user.

    Returns:
        float: The valid number entered by the user.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
