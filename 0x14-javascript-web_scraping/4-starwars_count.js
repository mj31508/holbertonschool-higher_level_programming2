#!/usr/bin/node

const request = require('request');
const arg = process.argv[2];

request(arg, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let json1 = (JSON.parse(body));
    let count = 0;
    for (let i in json1.results) {
      let a = json1.results[i].characters;
      for (let n in a) {
        if (a[n].includes('18')) {
          count++;
	}
      }
    }
    console.log(count);
  }
});
