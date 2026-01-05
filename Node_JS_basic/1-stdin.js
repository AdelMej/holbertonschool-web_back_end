console.log('Welcome to Holberton School, what is your name?');

let input = '';

process.stdin.on('data', (chunk) => {
  input += chunk;
});

process.stdin.on('end', () => {
  console.log(`Your name is: ${input}`);
  console.log('This important software is now closing');
});
