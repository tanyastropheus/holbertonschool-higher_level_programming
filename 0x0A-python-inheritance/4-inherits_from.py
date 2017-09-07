#!/usr/bin/python3
def inherits_from(obj, a_class):
    """check if an object is an instance of a subclass of the specified class.

    Args:
        obj: a given object
        a_class: the specified class

    Returns:
        True if the object is an instance of the subclass of a_class;
        False if the object is not an instance of the subclass of a_class,
    or the object is an instance of the specified class.

"""
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
