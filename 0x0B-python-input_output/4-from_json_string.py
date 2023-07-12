#!/usr/bin/python3
'''Converts a JSON string to the corresponding Python object (data structure).'''

import json


def from_json_string(my_str):
    '''Converts a JSON string to the corresponding Python object (data structure).

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        any: The Python object represented by the JSON string.
    '''
    return json.loads(my_str)
