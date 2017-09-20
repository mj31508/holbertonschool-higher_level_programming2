#!/usr/bin/node

// using recursion

let args = process.argv.slice(2);
function factorial (n) {
  if (n === 1 || isNaN(Number(n))) {
    return (1);
  } else {
    return factorial(n - 1) * n;
  }
}
console.log(factorial(args[0]));
