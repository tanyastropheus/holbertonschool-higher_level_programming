#!/usr/bin/node

let request = require('request');

const options = {
  url: 'http://swapi.co/api/films/' + process.argv[2],
  method: 'GET',
  headers: {
    'Accept': 'application/json',
    'Accept-Charset': 'utf-8'
  }
};

request(options, function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  let json = JSON.parse(body);
  console.log(json['title']);
});
