#!/usr/bin/node

let request = require('request');

request.get(process.argv[2]).on('response', function (response) {
  console.log('code:', response.statusCode);
});
