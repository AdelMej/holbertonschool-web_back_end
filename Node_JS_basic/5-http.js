const http = require('node:http');
const fs = require('node:fs');

function parseCsv(content) {
  const lines = content.trim().split('\n');
  const headers = lines[0].split(',');

  return lines.slice(1).map((line) => {
    const values = line.split(',');
    const obj = {};

    headers.forEach((header, i) => {
      obj[header] = values[i];
    });
    return obj;
  });
}

function groupByField(students) {
  const result = {};

  students.forEach((student) => {
    const { field } = student;

    if (!result[field]) {
      result[field] = [];
    }

    result[field].push(student.firstname);
  });
  return result;
}

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      let result = '';
      const students = parseCsv(data);

      result += `Number of students: ${students.length}\n`;

      const grouped = groupByField(students);

      Object.entries(grouped).forEach(([field, students]) => {
        result += `Number of students in ${field}: ${students.length}. List: ${students.join(', ')}\n`;
      });

      resolve(result.trim());
    });
  });
}

const app = http.createServer(async (req, res) => {
  if (req.url === '/') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello Holberton School!');
  }

  if (req.url === '/students') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');

    let output = 'This is the list of our students\n';
    output += await countStudents('database.csv');
    res.end(output);
  }
});

app.listen(1245);

module.exports = app;
