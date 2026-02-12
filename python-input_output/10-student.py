#!/usr/bin/python3
"""Module that defines a Student class with filtered JSON serialization."""


class Student:
    """Represents a student with first name, last name, and age."""
    
    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student."""
        if isinstance(attrs, list):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
