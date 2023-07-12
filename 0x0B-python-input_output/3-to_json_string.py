#!/usr/bin/python3
'''Converts an object to its JSON representation as a string.'''

import json


def to_json_string(my_obj):
    '''Converts an object to its JSON representation as a string.

    Args:
        my_obj (any): The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object as a string.
    '''
    return json.dumps(my_obj)
