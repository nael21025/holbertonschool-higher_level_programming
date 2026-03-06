#!/usr/bin/python3
"""Module for full-featured rectangle class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle shape that inherits from BaseGeometry.

    This class represents a rectangle with width and height, and can
    calculate its area and provide a string representation.
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

    def area(self):
        """Calculate and return the area of the rectangle.

        Returns:
            The area as width multiplied by height
        """
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle.

        Returns:
            A formatted string with the rectangle dimensions
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
