#!/usr/bin/python3
"""
function that reads a text file
"""


def read_file(filename=""):
    """Reads a text file (UTF-8) and prints its content to stdout.

    Args:
        filename (str): The path to the text file. (default: "")

    Returns:
        None
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
