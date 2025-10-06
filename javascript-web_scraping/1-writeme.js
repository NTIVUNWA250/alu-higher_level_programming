#!/usr/bin/node
const [, , fileA, contentA] = process.argv;
require('fs').writeFileSync(fileA, contentA, { encoding: 'utf-8' });
