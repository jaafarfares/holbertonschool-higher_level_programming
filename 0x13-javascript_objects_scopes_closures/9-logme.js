#!/usr/bin/node
let countt = 0;
exports.logMe = function (item) {
  console.log(`${countt}: ${item}`);
  countt += 1;
};
