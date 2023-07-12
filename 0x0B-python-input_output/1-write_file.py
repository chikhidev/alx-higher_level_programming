#!/usr/bin/python3
"""
function that writes a string to a text file (UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF-8) and return the number of characters written.

    Args:
        filename (str, optional): The name of the file to write to. Defaults to an empty string.
        text (str, optional): The string to write to the file. Defaults to an empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w') as f:
        return f.write(text)