#!/usr/bin/node
const { argv } = require('process');
if (isNaN(argv[2])) {
  console.log('Missing size');
} else {
  let square = '';
  for (let i = 0; i < (argv[2]); i++) {
    square += 'X';
  }
  for (let j = 0; j < (argv[2]); j++) {
    console.log(square);
  }
}
