#!/usr/bin/node
let count = 0;
module.exports = {
  logMe: (item) => {
    console.log(`${count++}: ${item}`);
  }
};
