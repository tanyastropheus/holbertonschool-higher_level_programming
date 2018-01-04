#!/usr/bin/node

exports.addMeMaybe = function (number, theFunction) {
  let x = number + 1;
  theFunction(x);
};
