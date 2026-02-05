#!/usr/bin/python3
"""Module for checking inherited classes"""


def inherits_from(obj, a_class):
    """Check if object is instance of a subclass, but not exactly that class.

    Args:
        obj: The object to check
        a_class: The class to compare against

    Returns:
        True if obj is instance of subclass of a_class, False otherwise
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
