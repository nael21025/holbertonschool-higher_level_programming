#!/usr/bin/python3
"""Module for converting class instances to JSON-serializable dictionaries."""


def class_to_json(obj):
    """Returns the dictionary description for JSON serialization of an object."""
    return obj.__dict__
