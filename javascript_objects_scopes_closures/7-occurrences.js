#!/usr/bin/node
module.exports = {
  nbOccurences: (list, searchElement) => {
    return list.reduce((acc, element) => element === searchElement ? ++acc : acc, 0);
  }
};
