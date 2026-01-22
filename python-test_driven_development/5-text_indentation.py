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
    skip_spaces = True
    while i < len(text):
        char = text[i]

        if char == ' ' and skip_spaces:
            i += 1
            continue

        if char in ".?:":
            print(char)
            print()
            skip_spaces = True
            # Skip the next character if it's a newline or tab
            if i + 1 < len(text) and text[i + 1] in '\n\t':
                i += 1
        elif char == '\n':
            print()
            skip_spaces = True
        elif char == '\t':
            print(char, end="")
            skip_spaces = False
        else:
            print(char, end="")
            skip_spaces = False

        i += 1
