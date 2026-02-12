#!/usr/bin/python3
"""Module that appends a string to a text file."""


def append_write(filename="", text=""):
    """Appends a string to a text file and returns the number of characters added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
