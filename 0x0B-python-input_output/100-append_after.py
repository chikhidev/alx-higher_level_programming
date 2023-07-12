#!/usr/bin/python3
"""
Inserts a line of text into a file after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    '''Inserts a line of text into a file after each line containing a specific string.

    Args:
        filename (str): The name of the file to update.
        search_string (str): The string to search for in each line.
        new_string (str): The line of text to insert after each matched line.

    Returns:
        None
    '''
    with open(filename, 'r+') as f:
        lines = f.readlines()
        i = 0
        for line in lines:
            if line.find(search_string) != -1:
                lines.insert(i + 1, new_string)
            i += 1
        f.seek(0)
        f.write("".join(lines))
