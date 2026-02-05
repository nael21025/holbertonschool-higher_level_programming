#!/usr/bin/python3
"""Module for custom list class"""


class MyList(list):
    """A list subclass with additional methods.

    Inherits from the built-in list class and provides
    functionality to print a sorted version of the list.
    """

    def print_sorted(self):
        """Print the list in ascending sorted order.

        The original list remains unchanged.
        Assumes all elements are of type int.
        """
        print(sorted(self))
