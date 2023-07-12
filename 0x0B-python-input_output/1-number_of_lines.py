#!/usr/bin/python3
''' function that returns the number of lines of a text file
'''


def number_of_lines(filename=""):
    """Count the number of lines in a text file.

    Args:
        filename (str, optional): The name of the file to count the lines of. Defaults to an empty string.

    Returns:
        int: The number of lines in the text file. Returns 0 if the filename is empty or not a string.
    """
    if filename == "" or type(filename) != str:
        return 0
    counter = 0
    with open(filename, 'r') as f:
        for line in f:
            counter += 1
    return counter
