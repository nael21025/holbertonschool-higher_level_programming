#!/usr/bin/python3
"""
This module provides a function for printing a square with the # character.
It validates that the size is an integer and is not negative.
The function prints the square to stdout.
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size: The size length of the square (must be an integer >= 0)

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
    """
    if type(size) is bool or not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
