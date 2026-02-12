#!/usr/bin/python3
"""Module for converting class instances to JSON-serializable dictionaries."""


def class_to_json(obj):
    """Returns dictionary with simple data structures for JSON serialization."""
    return obj.__dict__
