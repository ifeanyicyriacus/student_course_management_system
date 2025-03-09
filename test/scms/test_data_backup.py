import os
from unittest import TestCase
from src.scms.data_backup import DataBackup, FileHandler, Course, Enrollment, Student, Instructor

class TestDataLoader(TestCase):
    directory = "test"
    courses_file_path = f"./../data/{directory}/courses.txt"
    enrollments_file_path = f"./../data/{directory}/enrollments.txt"
    students_file_path = f"./../data/{directory}/students.txt"
    instructors_file_path = f"./../data/{directory}/instructors.txt"

    def setUp(self):
        DataBackup(self.courses_file_path, self.enrollments_file_path, self.students_file_path, self.instructors_file_path)
        self.courses_file_handler = FileHandler(self.courses_file_path)
        self.enrollment_file_handler = FileHandler(self.enrollments_file_path)
        self.student_file_handler = FileHandler(self.students_file_path)
        self.instructor_file_handler = FileHandler(self.instructors_file_path)

    def tearDown(self):
        os.remove(self.courses_file_path)
        os.remove(self.enrollments_file_path)
        os.remove(self.students_file_path)
        os.remove(self.instructors_file_path)

    def test_test_get_courses(self):
        course1 = Course("courseID1", "courseName1", "courseDescription1", "InstructorID1")
        course2 = Course("courseID2", "courseName2", "courseDescription2", "InstructorID2")
        DataBackup.add_to_courses(course1)
        DataBackup.add_to_courses(course2)
        courses:[str] = self.courses_file_handler.read()
        self.assertEqual(len(courses), 2)

    def test_add_to_enrollments(self):
        DataBackup.add_to_enrollments(Enrollment("courseID1", "studentID1", 78, "2025-03-09"))
        DataBackup.add_to_enrollments(Enrollment("courseID2", "studentID1", 70, "2025-02-09"))
        DataBackup.add_to_enrollments(Enrollment("courseID1", "studentID2", 80, "2025-01-09"))
        enrollments:[str] = self.enrollment_file_handler.read()
        self.assertEqual(len(enrollments), 3)

    def test_add_to_students(self):
        DataBackup.add_to_students(Student("studentID1, fullName1, ifeanyi@email.com, password1"))
        DataBackup.add_to_students(Student("studentID2, fullName2, email2@email.com, password2"))
        students:[str] = self.student_file_handler.read()
        self.assertEqual(len(students), 2)

    def test_add_to_instructors(self):
        DataBackup.add_to_instructors(Instructor("InstructorID1, fullName1, chibuzo@email.com, password1"))
        DataBackup.add_to_instructors(Instructor("InstructorID2, fullName2, sk@email.com, password2"))
        DataBackup.add_to_instructors(Instructor("InstructorID3, fullName3, chinedu@email.com, password3"))
        instructors:[str] = self.instructor_file_handler.read()
        self.assertEqual(len(instructors), 3)
