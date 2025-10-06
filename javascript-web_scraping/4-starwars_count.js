#!/usr/bin/node
const [, , URL] = process.argv;
require('request')(URL, (_, __, body) => {
  console.log(JSON.parse(body).results.reduce((count, film) => {
    return (film.characters.find((ele) => ele.match(/.*\/18\/$/))) ? ++count : count;
  }, 0));
});
