#!/usr/bin/node

/**
 * a function that returns the reversed version of a list
 * prototype: Prototype: exports.esrever = function (list)
 */

exports.esrever = function (list) {
    const revList = [];
    for (let i = list.length - 1; i >= 0; i--) {
        revList.push(list[i]);
    }
    return (revList);
}

