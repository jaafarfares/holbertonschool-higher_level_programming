#!/usr/bin/node
const { argv } = require('process');
if (isNaN(argv[2])) {
  console.log('Not a number');
} else if (argv[2]) {
  const ey = parseInt(argv[2]);
  console.log('My number: ' + ey);
} else {
  console.log('Not a number');
}
