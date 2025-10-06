#!/usr/bin/node
const [, , URL] = process.argv;
require('request')(URL, (_, res) => {
  console.log(`code: ${res.statusCode}`);
});
