#!/usr/bin/node

const num = Number(process.argv[2]);
if (Number.isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(process.argv[2], 10)}`);
}
