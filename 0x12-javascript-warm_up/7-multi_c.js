#!/usr/bin/node
const { argv } = require('process');
const myVar = 'C is fun';
for (let i = 0; i < argv[2]; i++) {
  console.log(myVar);
}
