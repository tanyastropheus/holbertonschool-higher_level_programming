#!/usr/bin/node

let request = require('request');
let fs = require('fs');

request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
