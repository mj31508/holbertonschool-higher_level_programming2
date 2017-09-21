#!/usr/bin/node

// finding the second biggest int

let num = process.argv.slice(2);

if (num.length === 0 || num.length === 1) {
  console.log(0);
} else {
  let MaXNuM = Number(num[0]);
  for (let j = 0; j < num.length; j++) {
    if (Number(num[j]) > MaXNuM) {
      MaXNuM = Number(num[j]);
    }
  }

  for (let i = 0; i < num.length; i++) {
    if (Number(num[i]) === MaXNuM) {
      num.splice(i, 1);
    }
  }

  let secmax = num[0];
  for (let j = 0; j < num.length; j++) {
    if (Number(num[j]) > secmax) {
      secmax = Number(num[j]);
    }
  }
  console.log(secmax);
}
