#!/usr/bin/node

const dict = require('./101-data.js');

const user_ids_by_occurrence = {};

for (const [user_id, occurrence] of dict.entries()) {
  if (!user_ids_by_occurrence.hasOwnProperty(occurrence)) {
    user_ids_by_occurrence[occurrence] = [];
}

  user_ids_by_occurrence[occurrence].push(user_id);
}

console.log(user_ids_by_occurrence);

