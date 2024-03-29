#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let p = '';
      for (let j = 0; j < this.width; j++) {
        p += 'X';
      }
      console.log(p);
    }
  }

  rotate () {
    const tmp = this.height;
    this.height = this.width;
    this.width = tmp;
  }

  double () {
    this.height = 2 * (this.height);
    this.width = 2 * (this.width);
  }
}
module.exports = Rectangle;
