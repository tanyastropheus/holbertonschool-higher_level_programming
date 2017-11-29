#!/usr/bin/python3
'''send a request to the URL & displays the body of response'''

import urllib.request
from sys import argv


if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(argv[1]) as response:
            content = response.read()
            print(content.decode('utf-8'))
    '''display HTTP status code'''
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
