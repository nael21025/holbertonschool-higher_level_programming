#!/usr/bin/python3
"""BaseGeometry module for geometry classes with validation."""


class BaseGeometry:
    """Geometry base class with validation and area methods."""

    def area(self):
        """Raises an exception indicating method is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer.

        Args:
            name: Name of the parameter to validate
            value: The value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is not greater than 0
        """
        if type(value) is not int or type(value) is bool:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
