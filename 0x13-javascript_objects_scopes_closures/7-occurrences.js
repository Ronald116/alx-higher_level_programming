#!/usr/bin/node
/**
 * a function that returns the occurrence of a list
 * prototype: exports.nbOccurences = function (list, searchElement)
*/

exports.nbOccurences = function (list, searchElement) {
    let count = 0;
    for (let i = 0; i < list.length; i++) {
        if (list[i] === searchElement) {
            count++;
        }
    }
    return (count);
}
