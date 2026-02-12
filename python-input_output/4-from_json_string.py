#!/usr/bin/python3
"""Module that converts JSON string to an object."""
import json


def from_json_string(my_str):
    """Return an object represented by a JSON string.
    
    Args:
        my_str: The JSON string to convert.
        
    Returns:
        Python object represented by the JSON string.
    """
    return json.loads(my_str)
