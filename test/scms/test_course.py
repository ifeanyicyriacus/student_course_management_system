import unittest
from src.scms.course import Course

class TestCourse(unittest.TestCase):
    course_id = "Test Course ID"
    course_name = "Python 101"
    course_description = "Introduction to Python"
    instructor_id = "I001"

    def setUp(self):
        self.course = Course(self.course_id, self.course_name, self.course_description, self.instructor_id)

    def test_that_course_is_initialized_correctly(self):
        self.assertEqual(self.course.course_id, self.course_id)
        self.assertEqual(self.course.course_name, self.course_name)
        self.assertEqual(self.course.course_description, self.course_description)
        self.assertEqual(self.course.instructor_id, self.instructor_id)

    def test_set_course_name(self):
        self.course.course_name = "Python 111"
        self.assertEqual(self.course.course_name, "Python 111")

    def test_set_course_description(self):
        self.course.course_description = "Advanced Python"
        self.assertEqual(self.course.course_description, "Advanced Python")

    def test_set_empty_course_id(self):
        with self.assertRaises(ValueError):
            self.course.course_id = ""

    def test_set_empty_course_name(self):
        with self.assertRaises(ValueError):
            self.course.course_name = ""

    def test_set_empty_course_description(self):
        with self.assertRaises(ValueError):
            self.course.course_description = ""

    def test_set_empty_instructor_id(self):
        with self.assertRaises(ValueError):
            self.course.instructor_id = ""

    def test_invalid_initialization(self):
        empty_value = ""
        with self.assertRaises(ValueError):
            course = Course(empty_value,"Python 101", "Introduction to Python", "I001")
        with self.assertRaises(ValueError):
            course = Course("course_id",empty_value, "Introduction to Python", "I001")
        with self.assertRaises(ValueError):
            course = Course("course_id","Python 101", empty_value, "I001")
        with self.assertRaises(ValueError):
            course = Course("course_id","Python 101", "Introduction to Python", empty_value)
