#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w === undefined || w <= 0 || h === undefined || h <= 0) {
      module.exports = class Rectangle {};
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    while (i < this.height) {
      console.log('X'.repeat(this.width));
      i++;
    }
  }
};
