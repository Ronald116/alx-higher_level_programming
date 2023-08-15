#!/usr/bin/node

/**
 * Square class that inherits from Square of 5-square.js
 * Create an instance method called charPrint(c) that 
 * prints the rectangle using the character c
 * If c is undefined, use the character X
 */

const baseSquare = require('./5-square.js')

class Square extends baseSquare {
    charPrint(c) {
        if (c === undefined) {
            c = 'X';
        }
        for (let i = 0; i < this.height; i++) {
            let character = '';
            for (let j = 0; j < this.width; j++) {
                character += c;
            }
            console.log(character);
        }
    }
}

module.exports = Square
