#!/usr/bin/python3
"""contains from_json_string function"""
import json


def from_json_string(my_str):
    """returns an object (Python data structure) represented by a JSON string

    Args:
        my_str: given JSON string

    Returns:
        an object convered from JSON string

    """
    return json.loads(my_str)
