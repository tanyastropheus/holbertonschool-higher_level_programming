#!/usr/bin/python3
def read_file(filename=""):
    """print out the entire content of a file to stdout using UTF8 encoding

    Args:
        filename (str): file to be printed

    """
    with open(filename, encoding="UTF8") as f:
        for line in f:
            print(line, end="")
