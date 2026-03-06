#!/usr/bin/python3
"""Module for square class with string representation"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square shape that inherits from Rectangle.

    A square is a special case of a rectangle where width and height
    are equal. Provides a custom string representation showing 'Square'
    instead of 'Rectangle'.
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

    def __str__(self):
        """Return a string representation of the square.

        Returns:
            A formatted string identifying it as a Square with its size
        """
        return "[Square] {}/{}".format(self._Rectangle__width,
                                       self._Rectangle__height)
