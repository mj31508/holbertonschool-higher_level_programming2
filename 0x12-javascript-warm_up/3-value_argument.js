#!/usr/bin/node
// print a message depending on the arg

let args = process.argv;
let NuMArgS = args.slice(2);
let ArGOnE = NuMArgS[0];

if (!ArGOnE) { console.log('No argument'); } else { console.log(ArGOnE); }
