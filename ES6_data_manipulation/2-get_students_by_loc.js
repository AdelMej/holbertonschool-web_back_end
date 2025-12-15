export default function getStudentsByLocation(studentList, location) {
  return studentList.filter((studentList) => studentList.location === location);
}
