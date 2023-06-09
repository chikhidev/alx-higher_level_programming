#!/usr/bin/python3
def no_c(my_string):
    string = ''
    for char in my_string:
        if char != ('c' || 'C'):
            string += char
    return string
