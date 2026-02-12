#!/usr/bin/python3
"""Module that defines a Student class."""


class Student:
    """Defines a student."""
    
    def __init__(self, first_name, last_name, age):
        """Initialize a student.
        
        Args:
            first_name: The first name of the student.
            last_name: The last name of the student.
            age: The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance.
        
        Args:
            attrs: List of attribute names to retrieve.
            
        Returns:
            Dictionary representation of the student.
        """
        if attrs is None:
            return self.__dict__
        return {k: v for k, v in self.__dict__.items() if k in attrs}
