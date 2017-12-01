#!/usr/bin/python3
'''send a POST request with data & displays the body of the response'''

import requests
from sys import argv

if __name__ == "__main__":
    try:
        r = requests.post(argv[1], data={'email': argv[2]})
        print(r.text)
    except:
        pass
