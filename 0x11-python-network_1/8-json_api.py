#!/usr/bin/python3
'''takes a letter and make a POST request with the letter as parameter'''

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        r = requests.post('http://0.0.0.0:5000/search_user', data={'q': ""})
    elif len(argv) > 1:
        r = requests.post(
            'http://0.0.0.0:5000/search_user', data={'q': argv[1]})

    content = r.json()
    if content:
        try:
            print("[{}] {}".format(content['id'], content['name']))
        except:
            print("Not a valid JSON")
    else:
        print("No result")
