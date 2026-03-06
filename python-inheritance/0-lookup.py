#!/usr/bin/python3
"""Module for attribute and method lookup"""


def lookup(obj):
    """Return a list of attributes and methods of an object.

    Args:
        obj: An object to inspect

    Returns:
        A list of available attributes and methods
    """
    return dir(obj)
