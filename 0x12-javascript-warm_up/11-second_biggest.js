#!/usr/bin/node

let array = process.argv.slice(2);
if (array.length === 0 || array.length === 1) {
  console.log(0);
} else {
  let SortedIntArray = array.sort().reverse().map(Number);
  console.log(SortedIntArray[1]);
}
