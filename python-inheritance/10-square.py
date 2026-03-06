#!/usr/bin/python3
"""Module for square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square shape that inherits from Rectangle.

    A square is a special case of a rectangle where width and height
    are equal. The size must be a positive integer.
    """

    def __init__(self, size):
        """Initialize a square with a size.

        Args:
            size: The size (width and height) of the square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is not greater than 0
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
