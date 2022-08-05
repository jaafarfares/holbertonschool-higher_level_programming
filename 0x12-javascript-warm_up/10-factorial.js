#!/usr/bin/node
const { argv } = require('process');
function factorial() {
if ((isNaN(argv[2]) || !argv[2]) || (parseInt(argv[2]) === 0)) {
    console.log(1);
  } else {
    const num = parseInt(argv[2]);
    console.log(factorial(num));
  }
}