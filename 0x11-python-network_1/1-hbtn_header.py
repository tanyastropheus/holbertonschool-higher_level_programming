#!/usr/bin/python3
'''make a request to the URL & display value of the variable'''

import urllib.request
from sys import argv

try:
    with urllib.request.urlopen(argv[1]) as response:
        print(response.getheader("X-Request-Id"))
except:
    pass
