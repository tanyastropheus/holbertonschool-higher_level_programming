#!/usr/bin/python3
def write_file(filename="", text=""):
    """count the number of lines in a text file

    Args:
        filename (str): file to be written
        text (str): string to write to filename

    Returns:
        number of characters written.

    """
    with open(filename, 'w', encoding="UTF8") as f:  # create the file
        return f.write(text)
