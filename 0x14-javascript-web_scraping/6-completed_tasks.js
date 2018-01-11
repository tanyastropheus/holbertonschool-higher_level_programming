#!/usr/bin/node

let request = require('request');

const options = {
  url: process.argv[2],
  method: 'GET',
  headers: {
    'Accept': 'application/json',
    'Accept-Charset': 'utf-8'
  }
};

request(options, function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  let json = JSON.parse(body); // list of dicts
  //  console.log("inside:", json);
  let userTaskNum = {};
  let tasksCompleted = json.filter(function (tasks) {
    if (tasks['completed']) {
      return true;
    }
  });
  //  console.log(newList);
  let i = 0;
  let userID = 1;
  let count = 0;
  while (i < tasksCompleted.length) {
    if (tasksCompleted[i]['userId'] === userID) {
      count++;
      //      console.log("user ID:", userID);
      //      console.log("count:", count);
    } else {
      userTaskNum[userID] = count;
      userID++;
      count = 1;
    }
    i++;
    if (i === tasksCompleted.length) {
      userTaskNum[userID] = count;
    }
  }
  console.log(userTaskNum);
});
