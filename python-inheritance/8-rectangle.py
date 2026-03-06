#!/usr/bin/python3
"""Module for rectangle class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle shape that inherits from BaseGeometry.

    This class represents a rectangle with width and height.
    Both dimensions must be positive integers.
    """

    def __init__(self, width, height):
        """Initialize a rectangle with width and height.

        Args:
            width: The width of the rectangle
            height: The height of the rectangle

        Raises:
            TypeError: If width or height is not an integer
            ValueError: If width or height is not greater than 0
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
