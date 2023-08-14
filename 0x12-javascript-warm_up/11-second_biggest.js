#!/usr/bin/node

const args = process.argv.slice(2);
const intArgs = [];

for (let i = 0; i < args.length; i++) {
    intArgs.push(parseInt(args[i]));
}

if (intArgs.length === 0 || intArgs.length === 1) {
    console.log(0);
} else {
    intArgs.sort((a, b) => b - a);
    console.log(intArgs[1]);
}

