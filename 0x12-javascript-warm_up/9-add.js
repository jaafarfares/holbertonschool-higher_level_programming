#!/usr/bin/node
const { argv } = require('process');

function add (a, b) {
  const sum = a + b;
  return sum;
}
console.log(add(argv[2], argv[3]));
