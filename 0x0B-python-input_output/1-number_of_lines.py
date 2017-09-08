#!/usr/bin/python3
def number_of_lines(filename=""):
    """count the number of lines in a text file

    Args:
        filename (str): file to be counted

    Returns:
        line_num (int): number of lines in the file.

    """
    line_num = 0
    with open(filename, encoding="UTF8") as f:
        for line in f:
            line_num += 1
    return line_num
