#!/usr/bin/python3
'''send a POST request with paramers & display the response'''

import urllib.request
import urllib.parse
from sys import argv

'''data to POST to the server'''
data = urllib.parse.urlencode({'email': argv[2]})
data = data.encode('ascii')

try:
    with urllib.request.urlopen(argv[1], data) as response:
        content = response.read()
        print(content.decode('utf-8'))
except:
    pass
