#!/usr/bin/node
const argv = process.argv;
const f = require('fs');

f.writeFile(argv[2], process.argv[], 'utf8', (err, content) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(content);
});
