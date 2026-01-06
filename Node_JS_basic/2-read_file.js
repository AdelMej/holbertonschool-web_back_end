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
  try {
    const data = fs.readFileSync(path, 'utf8');
    const students = parseCsv(data);
    console.log(`Number of students: ${students.length}`);

    const grouped = groupByField(students);

    Object.entries(grouped).forEach(([field, students]) => {
      console.log(`Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`);
    });
  } catch (err) {
    throw Error('Cannot load database');
  }
}

module.exports = countStudents;
