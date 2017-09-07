#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """check if an object is an instance of the class or its subclass

    Args:
        obj: a given object.
        a_class: a given class/

    Returns:
        True if the object is an instance of the class or its subclass;
        False if not.

    """
    return isinstance(obj, a_class)
