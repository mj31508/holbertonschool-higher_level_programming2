#!/usr/bin/node

exports.Rectangle = function Rectangle (w, h) {
  if ((w !== undefined && w > 0) && (h !== undefined && h > 0)) {
    this.width = w;
    this.height = h;
  }
  this.print = function () {
    for (let x = 0; x < this.height; x++) {
      console.log('X'.repeat(this.width));
    }
  };

  this.rotate = function () {
    let temp = this.width;
    this.width = this.height;
    this.height = temp;
  };

  this.double = function () {
    this.width *= 2;
    this.height *= 2;
  };
};
