#!/usr/bin/python3
"""Module for converting class instances to JSON-serializable dictionaries."""


def class_to_json(obj):
    """Retrieves the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization
    of an object.
    """
    return obj.__dict__
