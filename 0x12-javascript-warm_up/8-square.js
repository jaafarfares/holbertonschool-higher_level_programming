#!/usr/bin/node
const { argv } = require('process');
if (isNaN(argv[2])) {
  console.log('Missing size');
} else {
  let s = '';
  for (let i = 0; i < argv[2]; i++) {
    s += 'x';
  }
  for (let a = 0; a < argv[2]; a++) {
    console.log(s);
  }
}
