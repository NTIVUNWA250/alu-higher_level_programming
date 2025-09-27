#!/usr/bin/node
function getArgs () {
  const scriptArgs = process.argv.slice(2);
  return scriptArgs.length === 0 ? undefined : scriptArgs;
}

function getSecondLargest (elements = []) {
  if (elements.length <= 1) {
    return 0;
  }
  const nums = elements.map(Number);
  return nums.sort((a, b) => b - a)[1];
}

console.log(getSecondLargest(getArgs()));
