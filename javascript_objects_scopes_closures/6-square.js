#!/usr/bin/node
const Sq = require('./5-square');

class Square extends Sq {
  charPrint (c) {
    if (c) {
      console.log(`${c.repeat(this.width)}\n`.repeat(this.height).trimEnd());
    } else {
      super.print();
    }
  }
}
module.exports = Square;
