#!/bin/bash
# send a request to a URL & display only the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
