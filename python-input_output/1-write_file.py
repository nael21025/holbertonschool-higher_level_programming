#!/usr/bin/python3
"""Module that writes a string to a text file."""


def write_file(filename="", text=""):
    """Write a string to a text file and return number of characters written.
    
    Args:
        filename: The name of the file to write to.
        text: The text to write to the file.
        
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
