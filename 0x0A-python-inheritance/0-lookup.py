#!/usr/bin/python3
def lookup(obj):
    """find a list of available attributes and methods of an object

    Args:
        obj: a given object

    Returns:
        list of available attributes and methods of a given object

    """
    return dir(obj)
