#!/usr/bin/python3
"""Module that defines BaseGeometry class for geometric shapes."""


class BaseGeometry:
    """Class providing geometric validation and area calculation interface.

    This class serves as a base for derived geometric shape classes
    and provides validation methods for ensuring proper parameter values.
    """

    def area(self):
        """Calculate the geometric area of the shape.

        This method must be overridden in derived classes to provide
        the specific area calculation for each geometric shape.

        Raises:
            Exception: Indicates that this method must be implemented
                by subclasses with specific area calculation logic.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a value is a positive integer.

        Checks whether the provided value is an integer and greater
        than zero. Raises appropriate exceptions for invalid values.

        Args:
            name: The name of the parameter being validated
            value: The value to validate

        Raises:
            TypeError: Raised when value is not an integer type
            ValueError: Raised when value is less than or equal to zero
        """
        if type(value) is not int or type(value) is bool:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
