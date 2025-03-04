from unittest import TestCase
from scms.instructor import Instructor
from course import Course

class Student:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class TestCourse(TestCase):
    def setUp(self):
        self.instructor = Instructor('001', 'John Doe', 'Computer Science', 123)
        self.course = Course('1234', 'Computer Science', 'introduction to computer science', self.instructor)
        self.student = Student('123', 'Jane Smith')

    def test_enroll_student(self):
        self.course.enroll_student(self.student)
        self.assertEqual(self.student, self.course.students)
        self.assertEqual(self.student.user_id, self.course.grades)
        self.assertEqual(self.course.grades[self.student.user_id])



