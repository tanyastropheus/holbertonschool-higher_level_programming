#!/usr/bin/node

exports.esrever = function (list) {
  let index = list.length - 1;
  let reverseList = list.slice(index);
  while (index >= 0) {
    reverseList.push(list[index]);
    index--;
  }
  return reverseList;
};
