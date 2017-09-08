#!/usr/bin/python3
"""load_from_json_file function"""
from sys import argv
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

filename = "add_item.json"
try:
    l = load_from_json_file(filename)
except FileNotFoundError:  # if file does not exist it cannot be read
    l = []
for i in range(1, len(argv)):
    l.append(argv[i])
save_to_json_file(l, filename)
