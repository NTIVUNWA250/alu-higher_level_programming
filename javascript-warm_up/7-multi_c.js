#!/usr/bin/node
if (Number.isNaN(Number(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  const times = Number(process.argv[2]).toFixed(0);
  for (let t = 0; t < times; t++) {
    console.log('C is fun');
  }
}
