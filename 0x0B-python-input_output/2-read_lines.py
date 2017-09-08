#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """count the number of lines in a text file

    Args:
        filename (str): file to be counted
        nb_lines (int): number of lines to print

    Returns:
        line_num (int): number of lines in the file.

    """
    line_num = 0
    with open(filename, encoding="UTF8") as f:
        if nb_lines > 0:
            for line in f:
                if line_num < nb_lines:
                    print(line, end="")
                line_num += 1
        print(f.read(), end="")
