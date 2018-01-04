#!/usr/bin/node

if (+process.argv[2]) { // + operates on numbers; implicit conversion in js
  console.log('My number: %d', parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
