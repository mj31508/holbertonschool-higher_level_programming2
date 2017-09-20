#!/usr/bin/node
// print a message depending on the arg

let args = process.argv;
let num_args = args.slice(2);
let arg_one = num_args[0];

if (!arg_one) {console.log('No argument');} else {console.log(arg_one);}
