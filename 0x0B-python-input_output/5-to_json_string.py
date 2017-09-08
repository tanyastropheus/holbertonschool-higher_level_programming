#!/usr/bin/python3
"""contains to_json_string function"""
import json


def to_json_string(my_obj):
    """return the JSON resperesentation of an object

    Args:
        my_obj: given object

    Returns:
        JSON representation of an object.

    """
    return json.dumps(my_obj)
