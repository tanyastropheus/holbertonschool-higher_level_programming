#!/bin/bash
# send a POST request with file content & display body of the response
curl -s --header "Content-Type: application/json" -X POST --data "@$2" "$1"
