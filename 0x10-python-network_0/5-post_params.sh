#!/bin/bash
# send a POST request with variables & display the body of the response
curl -sd "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
