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
    if type(obj) == a_class:
        return True
    else:
        return False
