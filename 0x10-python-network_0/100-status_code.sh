#!/bin/bash
# send a request to a URL & display only the status code
curl -sI "$1" | grep "HTTP" | cut -d' ' -f2
