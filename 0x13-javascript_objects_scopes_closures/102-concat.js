#!/usr/bin/node

/**
 * a script that concatenates two files
 */

const fs = require('fs');

const sourceFilePath1 = process.argv[2];
const sourceFilePath2 = process.argv[3];
const destinationFilePath = process.argv[4];

fs.readFile(sourceFilePath1, 'utf8', (err1, data1) => {
    if (err1) {
        console.error(`Error reading ${sourceFilePath1}: ${err1}`);
        return;
    }

    fs.readFile(sourceFilePath2, 'utf8', (err2, data2) => {
        if (err2) {
            console.error(`Error reading ${sourceFilePath2}: ${err2}`);
            return;
        }

        const concatenatedContent = data1 + data2;

        fs.writeFile(destinationFilePath, concatenatedContent, 'utf8', (err3) => {
            if (err3) {
                console.error(`Error writing ${destinationFilePath}: ${err3}`);
                return;
            }
            console.log(`Concatenated content written to ${destinationFilePath}`);
        });
    });
});

