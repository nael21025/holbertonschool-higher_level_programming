#!/usr/bin/python3
"""Module that defines a Student class."""


class Student:
    """Defines a student."""
    
    def __init__(self, first_name, last_name, age):
        """Initializes a student with first_name, last_name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        if attrs is None:
            return self.__dict__
        return {k: v for k, v in self.__dict__.items() if k in attrs}
