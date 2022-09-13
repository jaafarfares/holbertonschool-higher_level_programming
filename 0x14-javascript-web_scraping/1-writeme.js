#!/usr/bin/node
const f = require('fs');

f.writeFile(process.argv[2], process.argv[3], 'utf8', (err, content) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(content);
});
