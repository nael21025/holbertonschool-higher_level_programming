#!/usr/bin/python3
"""Module that appends a string to a text file."""


def append_write(filename="", text=""):
    """Append a string to a text file and return number of characters added.
    
    Args:
        filename: The name of the file to append to.
        text: The text to append to the file.
        
    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
