#!/usr/bin/node

exports.Rectangle = function Rectangle (w, h) {
  if ((w === undefined && w <= 0) || (h === undefined && h <= 0)) {
    this.width = w;
    this.height = h;
  }
};
