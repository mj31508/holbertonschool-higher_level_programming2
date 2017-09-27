#!/usr/bin/node

const request = require('request');
const arg = process.argv[2];

request(arg, function (error, response, body) {
  json1 = (JSON.parse(body));
  let count = 0;
  for(i = 0; i < json1.count; i++) {
    let a = json1.results[i].characters
    if (a.includes('https://swapi.co/api/people/18/')) {
      count++
    }

      }
    console.log(count)
});
