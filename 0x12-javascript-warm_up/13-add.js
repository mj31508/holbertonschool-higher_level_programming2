#!/usr/bin/node

// returning two integers from a different file

exports.add = function (a, b) {
  let num1 = parseFloat(a);
  let num2 = parseFloat(b);
  return (num1 + num2);
};
