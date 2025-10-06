#!/usr/bin/node
const [, , id] = process.argv;
require('request')(`https://swapi-api.alx-tools.com/api/films/${id}`, (_, __, body) => {
  console.log(JSON.parse(body).title);
});
