#!/usr/bin/node

const arrayArg = process.argv.slice(2);

let secondMax = 0;
if (arrayArg.length > 1) {
  secondMax = arrayArg.sort(function (a, b) { return b - a; })[1];
}
console.log(secondMax);
