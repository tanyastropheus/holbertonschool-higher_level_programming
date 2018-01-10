#!/usr/bin/node
const SquareParent = require('./5-square');

module.exports = class Square extends SquareParent {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let i = 0;
      while (i < this.height) {
        console.log(c.repeat(this.width));
        i++;
      }
    }
  }
};
