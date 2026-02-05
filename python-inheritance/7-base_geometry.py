#!/usr/bin/python3
"""Module for geometry class with area method"""


class BaseGeometry:
    """Base class for geometry shapes.

    Provides a base implementation for geometric shapes with an area
    calculation method.
    """

    def area(self):
        """Calculate the area of the geometry shape.

        Raises:
            Exception: This method must be implemented by subclasses
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value is a positive integer.

        Args:
            name: Name of the parameter
            value: Value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is not greater than 0
        """
        if type(value) is not int or type(value) is bool:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
