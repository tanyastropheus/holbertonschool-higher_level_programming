#!/bin/bash
# take in a URL, sends a GET request and a header variable, and display the body of the message
curl -s --header "X-HolbertonSchool-User-Id: 98" "$1"
