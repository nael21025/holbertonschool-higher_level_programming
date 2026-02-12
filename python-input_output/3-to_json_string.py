#!/usr/bin/python3
"""Module that converts an object to JSON string."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object.
    
    Args:
        my_obj: The object to convert to JSON.
        
    Returns:
        JSON string representation of the object.
    """
    return json.dumps(my_obj)
