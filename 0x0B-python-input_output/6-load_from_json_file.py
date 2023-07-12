#!/usr/bin/python3
"""Reads a JSON file and returns the corresponding Python object."""

import json


def load_from_json_file(filename):
    """Reads a JSON file and returns the corresponding Python object.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        any: The Python object created from the JSON file.
    """
    with open(filename) as f:
        return json.load(f)
