import readDatabase from '../utils.js';

const dbPath = process.argv[2];

class StudentsController {
  static async getAllStudents(request, response) {
    try {
      const data = await readDatabase(dbPath);
      const fields = Object.keys(data);
      console.log(fields);

      fields.sort((a, b) => a.localeCompare(b, undefined, { sensitivity: 'base' }));

      const lines = [];
      lines.push('This is the list of our students');

      for (const field of fields) {
        const students = data[field];
        lines.push(`Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`);
      }

      response.status(200).send(lines.join('\n'));
    } catch (err) {
      response.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(request, response) {
    const { major } = request.params;

    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    try {
      const data = await readDatabase(dbPath);
      response.status(200).send(`List: ${data[major].join(', ')}`);
    } catch (err) {
      response.status(500).send('Cannot load the database');
    }
  }
}

export default StudentsController;
