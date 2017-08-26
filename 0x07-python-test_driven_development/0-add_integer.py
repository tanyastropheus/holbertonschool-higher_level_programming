#!/usr/bin/python3
def add_integer(a, b):
    """Function that adds two numbers together

    Args:
        a (int/float): the first number.
        b (int/float): the second number.

    Returns:
        int: sum of a and b

    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)

#    for op in (a, b):
#        if type(op) not in [int, float]:
#            raise TypeError("{} must be an integer".format(a))
#    return int(a) + int(b)
