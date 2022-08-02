#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let stringRectangle = '';
    for (let i = 1; i <= this.height; i++) {
      for (let j = 1; j <= this.width; j++) {
        stringRectangle += 'X';
      }
      stringRectangle += '\n';
    }
    console.log(stringRectangle);
  }
};
