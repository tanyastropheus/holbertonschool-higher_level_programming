#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me
# script should  cause the server to respond with a message containing You got me!
curl -s -o /dev/null 0.0.0.0:5000/catch_me -w "You got me!"
