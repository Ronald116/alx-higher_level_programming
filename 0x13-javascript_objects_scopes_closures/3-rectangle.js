#!/usr/bin/node

/**
 * a Rectangle class that defines a rectangle
 * Args:
 *      1. w: width of the rectangle
 *      2. h: height of rectangle
 * create empty object if w or h === 0 or not a positive integer
 * an instance method print() that prints the rectangle using character X
 */

class Rectangle {
    constructor (w, h) {
        if ((w > 0 && typeof w === 'number') && 
        (h > 0 && typeof h === 'number')) {
            this.width = w;
            this.height = h;
        }
    }

    print() {
        for (let i = 0; i < this.height; i++) {
            let character = '';
            for (let j = 0; j < this.width; j++) {
                character += 'X';
            }
            console.log(character);
        }
    }
}

module.exports = Rectangle
