#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """A class representing a geometry."""

    def area(self):
        """Raises an exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if value is positive integer."""
        if type(value) is not int or type(value) is bool:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
