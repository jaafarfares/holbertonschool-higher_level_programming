#!/usr/bin/node
exports.esrever = function (list) {
  const newa = [];
  for (let i = list.length - 1; i >= 0; i--) {
    newa.push(list[i]);
  }
  return newa;
};
