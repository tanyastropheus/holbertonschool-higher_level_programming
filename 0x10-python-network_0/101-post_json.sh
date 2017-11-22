#!/bin/bash
# send a POST request with file content & display body of the response
curl -sd "@$2" "$1"
