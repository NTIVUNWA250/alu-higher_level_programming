#!/usr/bin/node

const request = require('request');
const [, , URL] = process.argv;

request(URL, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  try {
    const data = JSON.parse(body);

    if (!Array.isArray(data)) {
      throw new Error('Expected an array of tasks');
    }

    const completedTasks = data.reduce((acc, task) => {
      if (task.completed) {
        acc[task.userId] = (acc[task.userId] || 0) + 1;
      }
      return acc;
    }, {});

    console.log(completedTasks);
  } catch (e) {
    console.error('Error parsing JSON or reducing:', e.message);
  }
});
