#!/usr/bin/python3
def remove_char_at(string, index):
    result = ""
    for i in range(len(string)):
        if i != index:
            result += string[i]
    return result
