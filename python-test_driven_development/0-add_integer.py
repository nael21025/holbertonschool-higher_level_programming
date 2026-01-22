#!/usr/bin/python3
"""
This module provides a function for adding two integers.
It includes type checking and conversion from float to int.
The function handles edge cases like infinity and NaN.
"""


def add_integer(a, b=98):
    """
    Adds two integers together.
    
    Args:
        a: First number (int or float)
        b: Second number (int or float), defaults to 98
    
    Returns:
        int: The addition of a and b
    
    Raises:
        TypeError: If a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    
    return a + b
