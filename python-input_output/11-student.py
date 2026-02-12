#!/usr/bin/python3
"""Module that defines a Student class with JSON serialization and deserialization."""


class Student:
    """Represents a student with first name, last name, and age."""
    
    def __init__(self, first_name, last_name, age):
        """Initialize student instance with first_name, last_name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only attributes in this list are retrieved.
        Otherwise, all attributes are retrieved.
        """
        if isinstance(attrs, list):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
    
    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.
        The dictionary key will be the public attribute name.
        The dictionary value will be the value of the public attribute.
        """
        for key, value in json.items():
            setattr(self, key, value)
