#!/usr/bin/python3
"""Safe list integers printing function."""


def safe_print_list_integers(my_list=[], x=0):
    """Print integers from list, skip other types.

    Args:
        my_list: List to print from
        x: Number of elements to access

    Returns:
        Real number of integers printed
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, ValueError):
            continue
    print()
    return count
