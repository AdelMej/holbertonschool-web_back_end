const express = require('express');
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

const app = express();
const PORT = 1245;
const database = process.argv[2];

app.get('/', (req, res) => {
  res.type('text').send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  let output = 'This is the list of our students\n';
  try {
    output += await countStudents(database);
  } catch (err) {
    output += err.message;
  }
  res.type('text').send(output);
});

app.listen(PORT);

module.exports = app;
