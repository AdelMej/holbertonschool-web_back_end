export default function updateStudentGradeByCity(studentList, city, newGrades) {
  // making a lookup table that associate id and grade
  const gradeById = newGrades.reduce((acc, g) => {
    acc[g.studentId] = g.grade;
	console.log(acc);
    return acc;
  }, {});

  // filtering by city then adding grades if they exist else N/A
  return studentList.filter((student) => student.location === city)
    .map(student => ({
      ...student,
      grade: gradeById[student.id] ?? 'N/A',
    }));
}
