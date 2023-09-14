#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let m = 0;
  while ((len - m) > 0) {
    const tmp = list[len];
    list[len] = list[m];
    list[m] = tmp;
    m++;
    len--;
  }
  return list;
};
