#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for _key, _value in list(a_dictionary.items()):
        if _value is value:
            a_dictionary.pop(_key)
    return a_dictionary
