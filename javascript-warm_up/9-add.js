#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const n1 = Number(process.argv[2]);
const n2 = Number(process.argv[3]);
console.log(add(n1, n2));
