import os
from unittest import TestCase

from src.scms.data_restore import DataRestore, FileHandler


class TestDataLoader(TestCase):
    directory = "test"
    courses_file_path = f"./../data/{directory}/courses.txt"
    enrollments_file_path = f"./../data/{directory}/enrollments.txt"
    students_file_path = f"./../data/{directory}/students.txt"
    instructors_file_path = f"./../data/{directory}/instructors.txt"

    def setUp(self):
        courses_file_handler = FileHandler(self.courses_file_path)
        courses_file_handler.write("courseID1, courseName1, courseDescription1, InstructorID1")
        courses_file_handler.write("courseID2, courseName2, courseDescription2, InstructorID2")
        courses_file_handler.write("courseID3, courseName3, courseDescription3, InstructorID3")
        enrollment_file_handler = FileHandler(self.enrollments_file_path)
        enrollment_file_handler.write("courseID1, studentID1, 78, 2025-03-09")
        enrollment_file_handler.write("courseID2, studentID1, 70, 2025-02-09")
        enrollment_file_handler.write("courseID1, studentID2, 80, 2025-01-09")
        student_file_handler = FileHandler(self.students_file_path)
        student_file_handler.write("studentID1, fullName1, ifeanyi@email.com, password1")
        student_file_handler.write("studentID2, fullName2, email2@email.com, password2")
        instructor_file_handler = FileHandler(self.instructors_file_path)
        instructor_file_handler.write("InstructorID1, fullName1, chibuzo@email.com, password1")
        instructor_file_handler.write("InstructorID2, fullName2, sk@email.com, password2")
        instructor_file_handler.write("InstructorID3, fullName3, chinedu@email.com, password3")

        data_restore = DataRestore(self.courses_file_path,
                                        self.enrollments_file_path,
                                        self.students_file_path,
                                        self.instructors_file_path)
        self.restored_data = data_restore.restore()



    def tearDown(self):
        os.remove(self.courses_file_path)
        os.remove(self.enrollments_file_path)
        os.remove(self.students_file_path)
        os.remove(self.instructors_file_path)

    def test_get_courses(self):
        courses = self.restored_data[0]
        self.assertEqual(len(courses), 3)
        self.assertEqual(courses[0].course_id, "courseID1")
        self.assertEqual(courses[0].course_name, "courseName1")
        self.assertEqual(courses[0].course_description, "courseDescription1")
        self.assertEqual(courses[0].instructor_id, "InstructorID1")
        self.assertEqual(courses[2].course_id, "courseID3")
        self.assertEqual(courses[2].course_name, "courseName3")
        self.assertEqual(courses[2].course_description, "courseDescription3")
        self.assertEqual(courses[2].instructor_id, "InstructorID3")

    def test_get_enrollments(self):
        enrollments = self.restored_data[1]
        self.assertEqual(len(enrollments), 3)
        self.assertEqual(enrollments[0].course_id, "courseID1")
        self.assertEqual(enrollments[0].student_id, "studentID1")
        self.assertEqual(enrollments[0].grade, 78)
        self.assertEqual(enrollments[0].timestamp, "2025-03-09")

    def test_get_students(self):
        students = self.restored_data[2]
        self.assertEqual(len(students), 2)
        self.assertEqual(students[0].student_id, "studentID1")
        self.assertEqual(students[0].full_name, "fullName1")
        self.assertEqual(students[0].email, "ifeanyi@email.com")
        self.assertTrue(students[0].verify_password("password1"))

    def test_get_instructors(self):
        instructors = self.restored_data[3]
        self.assertEqual(len(instructors), 3)
        self.assertEqual(instructors[0].email, "chibuzo@email.com")
        self.assertEqual(instructors[1].email, "sk@email.com")
        self.assertEqual(instructors[2].email, "chinedu@email.com")
