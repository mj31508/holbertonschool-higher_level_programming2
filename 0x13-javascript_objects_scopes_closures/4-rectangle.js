#!/usr/bin/node

exports.Rectangle = function Rectangle (w, h) {
  if ((w !== undefined && w > 0) && (h !== undefined && h > 0)) {
    this.width = w;
    this.height = h;

    this.print = function () {
      for (let x = 0; x < h; x++) {
      // for (let i = 0; i < w; i++) {
      // process.stdout.write('X');
        console.log('X'.repeat(w));
      // console.log(this.height);
      }
    };

    this.rotate = function () {
      let temp = w;
      w = h;
      h = temp;
    };

    this.double = function () {
      w *= 2;
      h *= 2;
    };
    console.log();
  }
};
