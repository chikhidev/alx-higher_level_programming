#!/usr/bin/python3
'''Writes a Python object to a text file using JSON representation.'''

import json


def save_to_json_file(my_obj, filename):
    '''Writes a Python object to a text file using JSON representation.

    Args:
        my_obj (any): The Python object to be saved.
        filename (str): The name of the file to save the JSON representation to.

    Returns:
        None
    '''
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
