const http = require('node:http');
const countStudents = require('./3-read_file_async');

const app = http.createServer(async (req, res) => {
  if (req.url === '/') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello Holberton School!');
  }

  if (req.url === '/students') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    try {
      let output = 'This is the list of our students\n';
      output += await countStudents('database.csv');
      res.end(output);
    } catch (err) {
      res.statusCode = 500;
      res.end(err.message);
    }
  }
});

app.listen(1245);

module.exports = app;
