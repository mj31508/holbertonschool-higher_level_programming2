#!/usr/bin/node

// checking for a number

let args = process.argv.splice(2);

if (isNaN(Number(args[0]))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + args[0]);
}
