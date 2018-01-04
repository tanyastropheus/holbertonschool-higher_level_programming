#!/usr/bin/node

let size = +process.argv[2];
let i = 0;

if (size) {
  while (i < size) {
    console.log('X'.repeat(size));
    i++;
  }
} else {
  console.log('Missing size');
}
