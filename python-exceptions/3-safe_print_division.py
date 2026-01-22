#!/usr/bin/python3
"""Safe division printing function."""


def safe_print_division(a, b):
    """Divide 2 integers safely.

    Args:
        a: Dividend
        b: Divisor

    Returns:
        Division result or None if error
    """
    result = None
    try:
        result = a / b
    except Exception:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
