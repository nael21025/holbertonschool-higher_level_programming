#!/usr/bin/python3
"""Module for geometry class with validation"""


class BaseGeometry:
    """Base class for geometry shapes with integer validation.

    Provides methods for calculating area and validating integer parameters
    for geometry shapes.
    """

    def area(self):
        """Calculate area of the geometry shape.

        Raises:
            Exception: This method must be overridden in subclass
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
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
