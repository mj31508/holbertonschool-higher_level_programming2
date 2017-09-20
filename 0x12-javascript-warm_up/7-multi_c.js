#!/usr/bin/node

// printing a script by multiples

if (parseFloat(process.argv[2])) {
  for (let num = 0; num < parseInt(process.argv[2]); num++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
