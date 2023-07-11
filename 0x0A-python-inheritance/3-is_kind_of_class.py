#!/usr/bin/python3
''' Module: 2-is_same_class
'''


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or a subclass of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare the type of obj with.

    Returns:
        bool: True if obj is an instance or subclass of a_class, False otherwise.
    """
    return isinstance(obj, a_class)
