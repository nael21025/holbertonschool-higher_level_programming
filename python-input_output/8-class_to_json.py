#!/usr/bin/python3
"""Defines a function to convert class instances to dictionaries."""


def class_to_json(obj):
    """Returns the dictionary representation of an object."""
    return obj.__dict__
