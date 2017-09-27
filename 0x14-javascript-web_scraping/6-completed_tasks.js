#!/usr/bin/node

const request = require('request');
const arg = process.argv[2];

request(arg, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let rdict = {};
    for (let uid of JSON.parse(body)) {
      if (uid.completed === true) {
        if (rdict.hasOwnProperty(uid.userId) === false) {
          rdict[uid.userId] = 1;
        } else {
          rdict[uid.userId] += 1;
        }
      }
      // rdict["userID"] =
   // let json1 = (JSON.parse(body));
    }
    console.log(rdict);
  }
});
