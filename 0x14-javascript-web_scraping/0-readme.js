#!/usr/bin/node
const f = require('fs');

f.readFile(process.argv[2], 'utf8', (err, content) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(content);
});
