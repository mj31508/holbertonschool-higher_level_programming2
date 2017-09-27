#!/usr/bin/node

let fs = require('fs');
let request = require('request');
let arg = process.argv[2];
let file = process.argv[3];
request(arg, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(file, body, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
