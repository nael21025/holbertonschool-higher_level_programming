#!/usr/bin/python3
"""Module that reads a text file and prints it to stdout."""


def read_file(filename=""):
    """Read a text file (UTF8) and print to stdout.
    
    Args:
        filename: The name of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
