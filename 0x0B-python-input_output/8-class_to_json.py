#!/usr/bin/python3
'''Converts a class object to a dictionary representation.'''

def class_to_json(obj):
    '''Converts a class object to a dictionary representation.

    Args:
        obj (object): The object to be converted to a dictionary.

    Returns:
        dict: A dictionary representing the object's attributes.
    '''
    return obj.__dict__
