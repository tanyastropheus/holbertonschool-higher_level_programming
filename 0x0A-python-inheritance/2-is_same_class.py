#!/usr/bin/python3
def is_same_class(obj, a_class):
    """checks if the object is exactly an instance of the specified class

    Args:
        obj: a given object.
        a_class: given class.

    Returns:
        True id the object is exactly an instance of the specified class;
        False if not.

    """

    return type(obj) == a_class
