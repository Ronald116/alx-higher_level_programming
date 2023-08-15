#!/usr/bin/node

/**
 * class Rectangle that defines a rectangle
 * Args:
 *      1. w: width of the rectangle
 *      2. h: height of the rectangle
 * create an empty object if w or h equal to 0 or not a positive integer
 * method print() that prints the rectangle using character 'X'
 * method rotate() that exchanges the width with the height
 * method double() that multiplies the width and height by 2
 */

class Rectangle {
    constructor (w,h) {
        if ((w > 0 && typeof w === 'number') && 
        (h > 0 && typeof h === 'number')) {
            this.width = w;
            this.height = h;
        }
    };

    print() {
        for (let i = 0; i < this.height; i++) {
            let character = '';
            for (let j = 0; j < this.width; j++) {
                character += 'X';
            };
            console.log(character);
        };
    };

    rotate() {
        this.width = this.width + this.height;
        this.height = this.width - this.height;
        this.width = this.width - this.height;
    };

    double() {
        this.width *= 2;
        this.height *= 2;
    }
};

module.exports = Rectangle
