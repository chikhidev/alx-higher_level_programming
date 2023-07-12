#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """Append a string to the end of a UTF-8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters appended to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
