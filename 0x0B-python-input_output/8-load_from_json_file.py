#!/usr/bin/python3
"""load_from_json_file function"""
import json


def load_from_json_file(filename):
    """creates an Object from a "JSON file"

    Args:
        filename: file to be written

    Returns:
        an object converted from a JSON string

    """
    with open(filename, 'r') as f:
        return json.loads(f.read())
