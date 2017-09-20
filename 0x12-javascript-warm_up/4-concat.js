#!/usr/bin/node
// printing two arguments

let args = process.argv.splice(2);
console.log(args[0] + ' is ' + args[1]);
