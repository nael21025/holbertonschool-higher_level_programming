#!/usr/bin/python3
"""
This module provides a function for formatting text with indentation.
It prints text with 2 new lines after each '.', '?', and ':' character.
No spaces are printed at the beginning or end of each printed line.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?', and ':'.
    
    Args:
        text: The text to format (must be a string)
    
    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
