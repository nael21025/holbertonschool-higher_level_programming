#!/usr/bin/python3
"""Defines a class that represents a student with JSON capabilities."""


class Student:
    """Represents a student with personal information."""
    
    def __init__(self, first_name, last_name, age):
        """Initializes a new Student with first name, last name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        if isinstance(attrs, list):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
