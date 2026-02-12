#!/usr/bin/python3
"""Module that converts a class instance to a dictionary."""


def class_to_json(obj):
    """Return the dictionary description for JSON serialization of an object.
    
    Args:
        obj: An instance of a class.
        
    Returns:
        Dictionary representation of the object.
    """
    return obj.__dict__
