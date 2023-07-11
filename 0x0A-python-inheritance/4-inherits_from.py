#!/usr/bin/python3
''' module: 4-inherits_from
'''


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class that directly or indirectly inherits from a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare the type of obj with.

    Returns:
        bool: True if obj is an instance of a class that inherits (directly or indirectly) from a_class, False otherwise.
    """
    return type(obj) != a_class and isinstance(obj, a_class)
