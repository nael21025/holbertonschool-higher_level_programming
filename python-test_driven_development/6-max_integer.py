#!/usr/bin/python3
"""
Module to find the max integer in a list
"""


def max_integer(list=[]):
    """
    Function to find and return the max integer in a list of integers.
    If the list is empty, returns None.

    Args:
        list: A list of integers

    Returns:
        The maximum integer in the list, or None if empty
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
