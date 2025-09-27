#!/usr/bin/node
module.exports = {
  converter: (base) => {
    return (num) => num.toString(base);
  }
};
