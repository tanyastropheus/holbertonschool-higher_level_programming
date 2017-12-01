#!/usr/bin/python3
'''make a URL request and displays body of the response (HTTP status code)'''

import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    try:
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.HTTPError:
        print("Error code:", r.status_code)
