#!/usr/bin/python3
"""Safe list printing function."""


def safe_print_list(my_list=[], x=0):
    """Print x elements of a list.

    Args:
        my_list: List to print from
        x: Number of elements to print

    Returns:
        Real number of elements printed
    """
    printed = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            printed += 1
        except IndexError:
            break
    print()
    return printed
