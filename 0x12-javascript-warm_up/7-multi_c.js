#!/usr/bin/node

let rep = +process.argv[2];
let i = 0;
const phrase = 'C is fun';
if (rep) {
  while (i < +process.argv[2]) {
    console.log(phrase);
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
