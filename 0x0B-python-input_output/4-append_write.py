#!/usr/bin/python3
def append_write(filename="", text=""):
    """append a string at the end of a text file

    Args:
        filename (str): file to be appended
        text (str): string to append to filename

    Returns:
        number of characters added.

    """
    with open(filename, 'a', encoding="UTF8") as f:  # create the file
        return f.write(text)   # this executes f.write() and returns the count
