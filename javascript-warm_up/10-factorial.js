#!/usr/bin/node
function fac (n) {
  if (n < 0) {
    return ('Not applicable');
  } else if (n === 0 || Number.isNaN(n) || n === 1) {
    return 1;
  } else {
    return fac(n - 1) * n;
  }
}

const num = Number(process.argv[2]);
console.log(fac(num));
