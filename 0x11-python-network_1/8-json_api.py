#!/usr/bin/python3
'''takes a letter and make a POST request with the letter as parameter'''

import requests
from sys import argv
import sys

if __name__ == "__main__":
    if len(argv) == 1:
        r = requests.post('http://0.0.0.0:5000/search_user', data={'q': ""})
    elif len(argv) > 1:
        r = requests.post(
            'http://0.0.0.0:5000/search_user', data={'q': argv[1]})
    try:
        content = r.json()
        id_num = content.get('id')
        name = content.get('name')
    except ValueError:
        print("Not a valid JSON")
        sys.exit()
    if id_num is None or name is None:
        print("No result")
    else:
        print("[{}] {}".format(id_num, name))
