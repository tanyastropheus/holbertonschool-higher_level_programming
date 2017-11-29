#!/usr/bin/python3
'''send request to the URL and display the value of the given variable'''

import requests
from sys import argv

if __name__ == "__main__":
    try:
        r = requests.get(argv[1])
        print(r.headers['X-Request-Id'])
    except:
        pass
