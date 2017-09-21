#!/usr/bin/node

// printing a square

let num = process.argv[2];
let n = 0;
let i = 0;
let sqr = '';

if (isNaN(parseInt(num))) {
  console.log('Missing size');
} else {
  while (n < num) {
    sqr += 'X';
    n++;
  }
  while (i < num) {
    console.log(sqr);
    i++;
  }
}
