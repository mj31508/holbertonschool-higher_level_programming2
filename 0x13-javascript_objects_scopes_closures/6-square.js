#!/usr/bin/node

const Square1 = require('./5-square.js').Square;

function Square (size) {
  Square1.call(this, size);
}

Square.prototype = Object.create(Square.prototype);
Square.constructor = Square;

Square.prototype.charPrint = function (c = 'X') {
  this.print(c);
};

exports.Square = Square;
