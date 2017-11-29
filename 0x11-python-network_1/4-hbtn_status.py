#!/usr/bin/python3
'''fetches the givein URL using Request package'''

import requests

if __name__ == "__main__":
    try:
        r = requests.get('https://intranet.hbtn.io/status')
        print("Body response:")
        print("\t- type:", type(r.text))
        print("\t- content:", r.text)
    except:
        pass
