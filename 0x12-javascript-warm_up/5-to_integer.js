#!/usr/bin/node

const nb = Number.parseInt(process.argv[2]);
if (nb) {
  console.log('My number:', nb);
} else {
  console.log('Not a number');
}
