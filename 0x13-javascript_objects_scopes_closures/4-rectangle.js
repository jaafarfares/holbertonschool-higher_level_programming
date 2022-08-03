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
    for (let i = 0; i < this.width; i++) {
      stringRectangle += 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(stringRectangle);
    }
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }

  rotate () {
    const h = this.height;
    const w = this.width;
    this.width = h;
    this.height = w;
  }
};
