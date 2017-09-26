#!/usr/bin/node

let fs = require('fs');
let arg = process.argv[2];
let arg2 = process.argv[3];
fs.writeFile(arg, arg2, 'utf-8', function (err) {
  if (err) {
    console.log(err);
  }
});
