#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """A function that prints out first name and last name

    Args:
        first_name (string): first name
        last_name (string): last name.  If not passed, defaults to ""

    Returns:
        None.

    Raises:
        TypeError: if first_name or last_name is not of string type.

    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is", first_name, last_name)
