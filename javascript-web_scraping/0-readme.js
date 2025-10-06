#!/usr/bin/node
const [, , fileA] = process.argv;
console.log(require('fs').readFileSync(fileA, { encoding: 'utf-8' }));
