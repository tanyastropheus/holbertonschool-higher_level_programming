#!/usr/bin/node

let request = require('request');

const options = {
  url: process.argv[2],
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
  let charWA = 'https://swapi.co/api/people/18/';
  let i = 0;
  let count = 0;
  while (i < json['results'].length) {
    // a list of characters for one episode
    let epChars = json['results'][i]['characters'];
    if (epChars.includes(charWA)) {
      count++;
    }
    i++;
  }
  console.log(count);
});
