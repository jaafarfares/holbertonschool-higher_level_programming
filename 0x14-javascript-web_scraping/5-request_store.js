#!/usr/bin/node
const argv = process.argv;
const fs = require('fs');
const request = require('request');

request(argv[2], argv[3], function (err, response, body) {
  if (err) {
    console.log(err);
  }
  fs.writeFile(argv[3], body, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
