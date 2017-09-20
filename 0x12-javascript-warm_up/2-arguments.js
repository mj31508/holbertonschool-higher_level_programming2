#!/usr/bin/node
// print a message depending on the arg

if (process.argv.length === 2) { console.log('No argument'); } else if (process.argv.length === 3) { console.log('Argument found'); } else { console.log('Arguments found'); }
