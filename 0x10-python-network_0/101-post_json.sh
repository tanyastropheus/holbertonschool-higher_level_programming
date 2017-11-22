#!/bin/bash
# send a POST request with file content & display body of the response
curl -s "$1" -d "@$2"
