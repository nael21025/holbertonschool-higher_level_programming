#!/usr/bin/python3
"""Module that saves an object to a JSON file."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation.
    
    Args:
        my_obj: The object to save.
        filename: The name of the file to save to.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
