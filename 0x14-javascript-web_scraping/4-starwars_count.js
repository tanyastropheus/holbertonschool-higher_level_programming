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
  let i = 0;
  let count = 0;
  while (i < json['results'].length) {
    // a list of characters for one episode
    let epChars = json['results'][i]['characters'];
    let j;
    for (j = 0; j < epChars.length; j++) {
      if (epChars[j].endsWith('/18/')) {
        count++;
      }
    }
    i++;
  }
  console.log(count);
});
