#!/usr/bin/python3
"""Basic serialization module"""
import json


def serialize_and_save_to_file(data, filename):
    """
        Serialize and save data to a JSON file
        - data: A Python Dictionary with data
        - filename: The filename of the output JSON file
    """
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
        Load and deserialize data from a JSON file
        - filename: The filename of the input JSON file
        Returns: A Python Dictionary with the deserialized JSON data
    """
    with open(filename, 'r') as f:
        return json.load(f)
