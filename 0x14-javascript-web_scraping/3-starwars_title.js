#!/usr/bin/node

const request = require('request');
let arg = 'http://swapi.co/api/films/' + process.argv[2];

request(arg, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body)['title']);
  }
});
