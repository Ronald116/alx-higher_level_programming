#!/usr/bin/node

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

function add(a,b) {
    return (a + b);
}

if (!NaN(a) && !NaN(b)) {
    console.log(add(a,b));
}