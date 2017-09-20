#!/usr/bin/node

// printing a script by multiples

if (parseFloat(process.argv[2])) {
  for (let x = 0; x < parseInt(process.argv[2]); x++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
