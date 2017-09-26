#!/usr/bin/node

const request = require('request');
let arg = process.argv[2];

request(arg, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
