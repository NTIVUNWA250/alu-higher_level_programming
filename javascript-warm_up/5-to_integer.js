#!/usr/bin/node
if (Number.isNaN(Number(process.argv[2]))) {
  console.log('Not a number');
} else {
  console.log(`My number: ${Number(process.argv[2]).toFixed(0)}`);
}
