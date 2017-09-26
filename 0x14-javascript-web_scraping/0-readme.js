#!/usr/bin/node

let fs = require('fs');
let arg = process.argv[2];
fs.readFile(arg, 'utf-8', function (err, data) {
  if (err) {
    process.stdout.write(err);
  } else {
    console.log(data);
  }
});
