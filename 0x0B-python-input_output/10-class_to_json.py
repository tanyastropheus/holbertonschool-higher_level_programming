#!/usr/bin/python3
def class_to_json(obj):
    """return the dict description for JSON serialization of an object"""
    return obj.__dict__
