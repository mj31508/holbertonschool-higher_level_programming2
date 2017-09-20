#!/usr/bin/node

// adding two parameters in a function

let args = process.argv.slice(2);

function add (a, b) {
  return Number(a) + Number(b);
}
console.log(add(args[0], args[1]));
