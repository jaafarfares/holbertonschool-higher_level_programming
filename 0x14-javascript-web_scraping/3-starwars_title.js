#!/usr/bin/node
const argv = process.argv;
const request = require('request');

request.get('https://swapi-api.hbtn.io/api/films/' + argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  }
    console.log(JSON.parse(body).title);
});
