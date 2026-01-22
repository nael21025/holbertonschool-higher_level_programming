#!/usr/bin/python3
"""Safe integer printing function."""


def safe_print_integer(value):
    """Print an integer safely.

    Args:
        value: Value to print as integer

    Returns:
        True if value is an integer, False otherwise
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
