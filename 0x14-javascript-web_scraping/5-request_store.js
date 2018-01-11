#!/usr/bin/node

let request = require('request');

const options = {
  url: process.argv[2],
  method: 'GET',
  headers: {
    //    'Accept': 'application/json',
    'Accept-Charset': 'utf-8'
  }
};

request(options, function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  console.log(body);
});
