#!/usr/bin/node

/**
 * function that converts any number from base 10 to another base
 */

exports.converter = function (base) {
    function convert(a) {
        return (a.toString(base));
    }
    return (convert);
}
