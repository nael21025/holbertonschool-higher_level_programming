#!/usr/bin/python3
"""Module that defines a Student class with JSON serialization."""


class Student:
    """Represents a student with first name, last name, and age."""
    
    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self):
        """Retrieves a dictionary representation of a Student."""
        return self.__dict__
