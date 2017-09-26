#!/usr/bin/node

let fs = require('fs');
let arg = process.argv[2];
fs.readFile(arg, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
