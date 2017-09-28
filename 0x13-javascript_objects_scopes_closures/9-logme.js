#!/usr/bin/node

let num = 0;
exports.logME = function (item) {
  console.log(num + ':' + item);
  num++;
};
