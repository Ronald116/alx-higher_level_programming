#!/usr/bin/node

/**
 * a function that prints the number of arguments already printed
 */

let counter = 0;
exports.logMe = function (item) {
    console.log(`${counter}: ${item}`);
    counter += 1;
}
