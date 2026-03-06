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
