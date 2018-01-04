#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n === 0) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}

let n = +process.argv[2];
console.log(factorial(n));
