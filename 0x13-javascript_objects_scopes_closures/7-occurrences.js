#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let counts = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      counts += 1;
    }
  }
  return counts;
};
