#!/bin/bash
# send a POST request with file content & display body of the response
curl -sX POST "$1" -d "@$2"
