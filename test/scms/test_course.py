import unittest
from src.scms.instructor import Instructor
from src.scms.course import Course
from src.scms.student import Student


class TestCourse(unittest.TestCase):
    # def setUp(self):
    #     self.instructor = Instructor('001', 'adebayo', 'adebayosamuel6667@gmail.com', 'password123')
    #     self.course = Course('1234', 'Computer Science', 'Introduction to Computer Science', self.instructor)
    #     self.student = Student('123', 'adebayo kehinde', "kenny@gmail.com", "password")
    #
    # def test_enroll_student(self):
    #     self.course.enroll_student(self.student)
    #     self.assertIn(self.student, self.course.students)
    #     self.assertIn(self.student.user_id, self.course.grades)
    #     self.assertEqual(self.course.grades[self.student.user_id], None)
    def test_that_course_is_initialized_correctly(self):
        course = Course("Python 101", "Introduction to Python", "I001")
        self.assertEqual(course.course_name, "Python 101")
        self.assertEqual(course.course_description, "Introduction to Python")
        self.assertEqual(course.instructor_id, "I001")

    def test_set_course_name(self):
        course = Course("Python 101", "Introduction to Python", "I001")
        course.course_name = "Python 111"
        self.assertEqual(course.course_name, "Python 111")

    def test_set_course_description(self):
        course = Course("Python 101", "Introduction to Python", "I001")
        course.course_description = "Advanced Python"
        self.assertEqual(course.course_description, "Advanced Python")

    def test_set_empty_course_description(self):
        course = Course("Python 101", "Introduction to Python", "I001")
        with self.assertRaises(ValueError):
            course.course_description = ""

    # def test_invalid_initialization(self):
    #     course = Course("Python 101", "Introduction to Python", "I001")
    #     with self.assertRaises(ValueError):
    #         course.course_name = "wrong course name"
