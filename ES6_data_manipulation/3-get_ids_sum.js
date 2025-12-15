export default function getStudentIdsSum(studentList) {
  return studentList.reduce((sum, element) => sum + element.id, 0);
}
