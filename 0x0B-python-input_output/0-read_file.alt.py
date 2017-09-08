#!/usr/bin/python3
def read_file(filename=""):
    """print out the entire content of a file to stdout using UTF8 encoding

    Args:
        filename (str): file to be printed

    """
    try:
        with open(filename, encoding='UTF8') as f:
            print(f.read(), end="")
    except (TypeError, IOError):
        print("Please enter a valid file name")
